# Windows 10 add-on update and config facility
# Copyright 2017 Joseph Lee, released under GPL.

# Add-on configuration and updates.
# Because the add-on employs continuous delivery model, it is beneficial to provide update facility.
# Base config section was inspired by Read Feeds (Noelia Martinez).
# Overall update check routine comes from StationPlaylist Studio add-on (Joseph Lee).)

import os
import threading
import urllib
import tempfile
import hashlib
import ctypes.wintypes
import ssl
import time
import re
import config
import gui
import wx
import addonHandler
import updateCheck
import winUser

# Add-on config database
confspec = {
	"autoUpdateCheck": "boolean(default=true)",
	"updateChannel": "string(default=dev)",
	"updateCheckTime": "integer(default=0)",
	"updateCheckTimeInterval": "integer(min=0, max=30, default=1)",
}
config.conf.spec["wintenApps"] = confspec

_addonDir = os.path.join(os.path.dirname(__file__), "..", "..")
addonVersion = addonHandler.Addon(_addonDir).manifest['version']
addonUpdateCheckInterval = 86400

channels={
	"stable":"http://addons.nvda-project.org/files/get.php?file=w10",
	"dev":"http://addons.nvda-project.org/files/get.php?file=w10-dev",
}

def updateQualify(url):
	version = re.search("wintenApps-(?P<version>.*).nvda-addon", url.url).groupdict()["version"]
	return None if version == addonVersion else version

updateChecker = None
# To avoid freezes, a background thread will run after the global plugin constructor calls wx.CallAfter.
def autoUpdateCheck():
	currentTime = time.time()
	whenToCheck = config.conf["wintenApps"]["updateCheckTime"]
	if currentTime >= whenToCheck:
		threading.Thread(target=addonUpdateCheck, kwargs={"autoCheck":True}).start()
	else:
		global updateChecker
		updateChecker = wx.PyTimer(autoUpdateCheck)
		updateChecker.Start(whenToCheck-currentTime, True)

progressDialog = None
def addonUpdateCheck(autoCheck=False):
	global progressDialog
	config.conf["wintenApps"]["updateCheckTime"] = int(time.time()) + config.conf["wintenApps"]["updateCheckTimeInterval"] * addonUpdateCheckInterval
	updateCandidate = False
	updateURL = channels[config.conf["wintenApps"]["updateChannel"]]
	try:
		url = urllib.urlopen(updateURL)
		url.close()
	except IOError:
		if not autoCheck:
			wx.CallAfter(progressDialog.done)
			progressDialog = None
			# Translators: Error text shown when add-on update check fails.
			wx.CallAfter(gui.messageBox, _("Error checking for update."), _("Windows 10 App Essentials update"), wx.ICON_ERROR)
		return
	if not autoCheck:
		wx.CallAfter(progressDialog.done)
		progressDialog = None
	if url.code != 200:
		if not autoCheck:
			# Translators: Text shown when update check fails for some odd reason.
			wx.CallAfter(gui.messageBox, _("Add-on update check failed."), _("Windows 10 App Essentials update"))
		return
	else:
		# Am I qualified to update?
		qualified = updateQualify(url)
		if qualified is None:
			if not autoCheck:
				# Translators: Presented when no add-on update is available.
				wx.CallAfter(gui.messageBox, _("No add-on update available."), _("Windows 10 App Essentials update"))
			return
		else:
			# Translators: Text shown if an add-on update is available.
			checkMessage = _("Windows 10 App Essentials {newVersion} is available. Would you like to update?").format(newVersion = qualified)
			# Translators: Title of the add-on update check dialog.
			wx.CallAfter(getUpdateResponse, checkMessage, _("Windows 10 App Essentials update"), updateURL)

def getUpdateResponse(message, caption, updateURL):
	if gui.messageBox(message, caption, wx.YES_NO | wx.NO_DEFAULT | wx.CANCEL | wx.CENTER | wx.ICON_QUESTION) == wx.YES:
		W10UpdateDownloader([updateURL]).start()

class WinTenAppsConfigDialog(wx.Dialog):

	def __init__(self, parent):
		# Translators: The title of a dialog to configure advanced WinTenApps add-on options such as update checking.
		super(WinTenAppsConfigDialog, self).__init__(parent, title=_("Windows 10 App Essentials settings"))

		mainSizer = wx.BoxSizer(wx.VERTICAL)
		w10Helper = gui.guiHelper.BoxSizerHelper(self, orientation=wx.VERTICAL)

		# Translators: A checkbox to toggle automatic add-on updates.
		self.autoUpdateCheckbox=w10Helper.addItem(wx.CheckBox(self,label=_("Automatically check for add-on &updates")))
		self.autoUpdateCheckbox.SetValue(config.conf["wintenApps"]["autoUpdateCheck"])
		# Translators: The label for a setting in WinTenApps add-on settings to select automatic update interval in days.
		self.updateInterval=w10Helper.addLabeledControl(_("Update &interval in days"), gui.nvdaControls.SelectOnFocusSpinCtrl, min=0, max=30, initial=config.conf["wintenApps"]["updateCheckTimeInterval"])
		# Translators: The label for a combo box to select update channel.
		labelText = _("&Add-on update channel:")
		self.channels=w10Helper.addLabeledControl(labelText, wx.Choice, choices=["development", "stable"])
		self.updateChannels = ("dev", "stable")
		self.channels.SetSelection(self.updateChannels.index(config.conf["wintenApps"]["updateChannel"]))
		# Translators: The label of a button to check for add-on updates.
		updateCheckButton = w10Helper.addItem(wx.Button(self, label=_("Check for add-on &update")))
		updateCheckButton.Bind(wx.EVT_BUTTON, self.onUpdateCheck)

		w10Helper.addDialogDismissButtons(self.CreateButtonSizer(wx.OK | wx.CANCEL))
		self.Bind(wx.EVT_BUTTON, self.onOk, id=wx.ID_OK)
		self.Bind(wx.EVT_BUTTON, self.onCancel, id=wx.ID_CANCEL)
		mainSizer.Add(w10Helper.sizer, border=gui.guiHelper.BORDER_FOR_DIALOGS, flag=wx.ALL)
		mainSizer.Fit(self)
		self.Sizer = mainSizer
		self.autoUpdateCheckbox.SetFocus()
		self.Center(wx.BOTH | wx.CENTER_ON_SCREEN)

	def onOk(self, evt):
		global updateChecker
		if updateChecker and updateChecker.IsRunning(): updateChecker.Stop()
		config.conf["wintenApps"]["autoUpdateCheck"] = self.autoUpdateCheckbox.Value
		config.conf["wintenApps"]["updateCheckTimeInterval"] = self.updateInterval.Value
		if not self.updateInterval.Value:
			config.conf["wintenApps"]["updateCheckTime"] = 0
			updateChecker = None
		else:
			updateChecker = wx.PyTimer(autoUpdateCheck)
			currentTime = time.time()
			whenToCheck = currentTime+(self.updateInterval.Value * addonUpdateCheckInterval)
			updateChecker.Start(whenToCheck-currentTime, True)
		config.conf["wintenApps"]["updateChannel"] = ("dev", "stable")[self.channels.GetSelection()]
		self.Destroy()

	def onCancel(self, evt):
		self.Destroy()

	def onUpdateCheck(self, evt):
		self.onOk(None)
		global progressDialog
		progressDialog = gui.IndeterminateProgressDialog(gui.mainFrame,
		# Translators: The title of the dialog presented while checking for add-on updates.
		_("Add-on update check"),
		# Translators: The message displayed while checking for newer version of WinTenApps add-on.
		_("Checking for new version of Windows 10 App Essentials add-on..."))
		threading.Thread(target=addonUpdateCheck).start()

def onConfigDialog(evt):
	gui.mainFrame._popupSettingsDialog(WinTenAppsConfigDialog)


# Update downloader (credit: NV Access)
# Customized for WinTenApps add-on.

#: The download block size in bytes.
DOWNLOAD_BLOCK_SIZE = 8192 # 8 kb

def checkForUpdate(auto=False):
	"""Check for an updated version of NVDA.
	This will block, so it generally shouldn't be called from the main thread.
	@param auto: Whether this is an automatic check for updates.
	@type auto: bool
	@return: Information about the update or C{None} if there is no update.
	@rtype: dict
	@raise RuntimeError: If there is an error checking for an update.
	"""
	params = {
		"autoCheck": auto,
		"version": versionInfo.version,
		"versionType": versionInfo.updateVersionType,
		"osVersion": winVersion.winVersionText,
		"x64": os.environ.get("PROCESSOR_ARCHITEW6432") == "AMD64",
		"language": languageHandler.getLanguage(),
		"installed": config.isInstalledCopy(),
	}
	url = "%s?%s" % (CHECK_URL, urllib.urlencode(params))
	try:
		res = urllib.urlopen(url)
	except IOError as e:
		if isinstance(e.strerror, ssl.SSLError) and e.strerror.reason == "CERTIFICATE_VERIFY_FAILED":
			# #4803: Windows fetches trusted root certificates on demand.
			# Python doesn't trigger this fetch (PythonIssue:20916), so try it ourselves
			_updateWindowsRootCertificates()
			# and then retry the update check.
			res = urllib.urlopen(url)
		else:
			raise
	if res.code != 200:
		raise RuntimeError("Checking for update failed with code %d" % res.code)
	info = {}
	for line in res:
		line = line.rstrip()
		try:
			key, val = line.split(": ", 1)
		except ValueError:
			raise RuntimeError("Error in update check output")
		info[key] = val
	if not info:
		return None
	return info


class W10UpdateDownloader(updateCheck.UpdateDownloader):
	"""Overrides NVDA Core's downloader.)
	No hash checking for now, and URL's and temp file paths are different.
	"""

	def __init__(self, urls, fileHash=None):
		"""Constructor.
		@param urls: URLs to try for the update file.
		@type urls: list of str
		@param fileHash: The SHA-1 hash of the file as a hex string.
		@type fileHash: basestring
		"""
		super(W10UpdateDownloader, self).__init__(urls, fileHash)
		self.urls = urls
		self.destPath = tempfile.mktemp(prefix="stationPlaylist_update-", suffix=".nvda-addon")
		self.fileHash = fileHash

	def start(self):
		"""Start the download.
		"""
		self._shouldCancel = False
		# Use a timer because timers aren't re-entrant.
		self._guiExecTimer = wx.PyTimer(self._guiExecNotify)
		gui.mainFrame.prePopup()
		# Translators: The title of the dialog displayed while downloading add-on update.
		self._progressDialog = wx.ProgressDialog(_("Downloading Add-on Update"),
			# Translators: The progress message indicating that a connection is being established.
			_("Connecting"),
			# PD_AUTO_HIDE is required because ProgressDialog.Update blocks at 100%
			# and waits for the user to press the Close button.
			style=wx.PD_CAN_ABORT | wx.PD_ELAPSED_TIME | wx.PD_REMAINING_TIME | wx.PD_AUTO_HIDE,
			parent=gui.mainFrame)
		self._progressDialog.Raise()
		t = threading.Thread(target=self._bg)
		t.daemon = True
		t.start()

	def _error(self):
		self._stopped()
		gui.messageBox(
			# Translators: A message indicating that an error occurred while downloading an update to NVDA.
			_("Error downloading add-on update."),
			_("Error"),
			wx.OK | wx.ICON_ERROR)

	def _downloadSuccess(self):
		self._stopped()
		# Translators: The message presented when the update has been successfully downloaded
		# and is about to be installed.
		gui.messageBox(_("Add-on update downloaded. It will now be installed."),
			# Translators: The title of the dialog displayed when the update is about to be installed.
			_("Install Add-on Update"))
		from gui import addonGui
		wx.CallAfter(addonGui.AddonsDialog.handleRemoteAddonInstall, self.destPath.decode("mbcs"))


# These structs are only complete enough to achieve what we need.
class CERT_USAGE_MATCH(ctypes.Structure):
	_fields_ = (
		("dwType", ctypes.wintypes.DWORD),
		# CERT_ENHKEY_USAGE struct
		("cUsageIdentifier", ctypes.wintypes.DWORD),
		("rgpszUsageIdentifier", ctypes.c_void_p), # LPSTR *
	)

class CERT_CHAIN_PARA(ctypes.Structure):
	_fields_ = (
		("cbSize", ctypes.wintypes.DWORD),
		("RequestedUsage", CERT_USAGE_MATCH),
		("RequestedIssuancePolicy", CERT_USAGE_MATCH),
		("dwUrlRetrievalTimeout", ctypes.wintypes.DWORD),
		("fCheckRevocationFreshnessTime", ctypes.wintypes.BOOL),
		("dwRevocationFreshnessTime", ctypes.wintypes.DWORD),
		("pftCacheResync", ctypes.c_void_p), # LPFILETIME
		("pStrongSignPara", ctypes.c_void_p), # PCCERT_STRONG_SIGN_PARA
		("dwStrongSignFlags", ctypes.wintypes.DWORD),
	)

# Borrowed from NVDA Core (the only difference is the URL).
def _updateWindowsRootCertificates():
	crypt = ctypes.windll.crypt32
	# Get the server certificate.
	sslCont = ssl._create_unverified_context()
	u = urllib.urlopen("https://www.nvaccess.org/nvdaUpdateCheck", context=sslCont)
	cert = u.fp._sock.getpeercert(True)
	u.close()
	# Convert to a form usable by Windows.
	certCont = crypt.CertCreateCertificateContext(
		0x00000001, # X509_ASN_ENCODING
		cert,
		len(cert))
	# Ask Windows to build a certificate chain, thus triggering a root certificate update.
	chainCont = ctypes.c_void_p()
	crypt.CertGetCertificateChain(None, certCont, None, None,
		ctypes.byref(CERT_CHAIN_PARA(cbSize=ctypes.sizeof(CERT_CHAIN_PARA),
			RequestedUsage=CERT_USAGE_MATCH())),
		0, None,
		ctypes.byref(chainCont))
	crypt.CertFreeCertificateChain(chainCont)
	crypt.CertFreeCertificateContext(certCont)
