# WinTenApps/music_ui.py
# Part of Windows 10 App Essentials collection
# Copyright 2016 Joseph Lee, released under GPL.

# Various workarounds for Groove music.

import appModuleHandler
import controlTypes
from NVDAObjects.UIA import UIA
from globalPlugins.wintenObjs import SearchField

class AppModule(appModuleHandler.AppModule):

	def chooseNVDAObjectOverlayClasses(self, obj, clsList):
		if obj.UIAElement.cachedClassName in ("TextBox", "RichEditBox") and obj.UIAElement.cachedAutomationID == "SearchTextBox":
			clsList.insert(0, SearchField)
