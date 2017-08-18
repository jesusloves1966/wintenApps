# Windows 10 App Essentials #

* Tekijät: Joseph Lee, Derek Riemer sekä muut Windows 10:n käyttäjät
* Lataa [vakaa versio][1]
* Lataa [kehitysversio][2]

Tämä lisäosa sisältää kokoelman sovellusmoduuleja Windows 10:n mukana
tuleville sovelluksille sekä korjauksia tietyille säätimille.

Kokoelmaan sisältyvät seuraavat sovellus- tai tukimoduulit (katso tiedot
käytettävissä olevista ominaisuuksista kunkin sovelluksen kappaleesta):

* Hälytykset ja kello
* Kalenteri
* Laskin (moderni)
* Cortana
* Pelipalkki
* Groove Music
* Sähköposti
* Kartat
* Microsoft Edge
* Ihmiset
* Asetukset (järjestelmän asetukset, Windows+I)
* Skype (universaali sovellus)
* Kauppa
* Sää
* Sekalaisia moduuleita sellaisille säätimille kuin Käynnistä-valikon
  tiilet.

Huom: Tämä lisäosa edellyttää Windows 10:n versiota 1607 (koontiversio
14393) tai uudempaa ja NVDA 2017.1:tä tai uudempaa. Käytä parhaan
käyttökokemuksen varmistamiseksi viimeisintä vakaata koontiversiota (15063)
sekä uusinta vakaata NVDA:n versiota. Varmista myös, että tallennat NVDA:n
asetukset muutettuasi lisäosan päivitysasetuksia.

Tärkeä huomautus: Koska NVDA 2017.3:een on tehty muutoksia, jotka eivät ole
taaksepäin yhteensopivia, lisäosan versio 17.09 ja sitä uudemmat eivät toimi
NVDA:n 2017.3:a vanhemmissa versioissa.

## Yleistä

* Alavalikot tunnistetaan oikein Käynnistä-valikon tiilien pikavalikoissa.
* Tietyt valintaikkunat tunnistetaan nyt asianmukaisesti
  valintaikkunoiksi. Tällaisia ovat esim. Insider-esiversioiden
  valintaikkuna (Asetukset-sovelluksessa) sekä uudentyylinen Käyttäjätilien
  valvonnan valintaikkuna koontiversiossa 14328 ja uudemmissa NVDA
  2016.2.1:tä tai vanhempaa käytettäessä.
* Tiettyjen hakukenttien ehdotusten ilmestyminen/sulkeutuminen (varsinkin
  Asetukset- ja Kauppa-sovelluksissa) ilmaistaan nyt äänimerkeillä ja
  pistekirjoituksella. Tämä koskee myös Käynnistä-valikon hakukenttää. Nämä
  muutokset sisältyvät NVDA:han versiosta 2017.3 alkaen.
* NVDA voi ilmoittaa ehdotusten määrän useimmissa tapauksissa hakua
  suoritettaessa. Tätä toimintoa hallitaan "Lue objektien sijaintitiedot"
  -asetuksella Objektien lukuasetukset -valintaikkunasta.
* Sijaintitietoja (esim. 1 / 2) ei enää lueta tietyissä pikavalikoissa
  (kuten Edgessä).
* Seuraavat UIA-tapahtumat tunnistetaan: Ohjain kohteelle, aktiivisen alueen
  muutos, järjestelmän ilmoitus, elementti valittu, ikkuna avattu.
* Lisätty lisäosan päivitysmahdollisuus (automaattinen tai manuaalinen)
  NVDA:n Asetukset-valikosta löytyvän uuden Windows 10 App Essentials
  -valintaikkunan kautta. Vakaat ja kehitysversiot suorittavat oletuksena
  automaattisen päivitystarkistuksen viikoittain tai päivittäin.
* Mahdollisuus Universal Windows Platform (UWP) -sovelluksista tulevien
  tapahtumien seuraamiseen, mikäli NVDA:ta käytetään
  virheenkorjaus-lokitasolla.
* Tuki Fall Creators -päivityksen kelluvalle emojiensyöttöruudulle (käytä
  parhaan kokemuksen saamiseksi Windows OneCore -syntetisaattoria).
* Joidenkin sovellusten Aktiivisen alueen teksti luetaan. Näitä ovat
  mm. Edgen ilmoitukset ja laskutoimitusten tulokset Laskimessa sekä
  muut. Huomaa, että tämä saattaa johtaa joissakin tapauksissa ilmoitusten
  kahdesti puhumiseen. Suurin osa näistä muutoksista sisältyy NVDA
  2017.3:een.
* Ilmoitusruutuja ei puhuta enää moneen kertaan Creators-päivityksessä ja
  uudemmissa. Tämä korjaus sisältyy NVDA 2017.3:een.

## Hälytykset ja kello

* Ajanvalitsimen arvot puhutaan - havaittavissa siirrettäessä kohdistusta
  valitsimen säätimiin. Tämä vaikuttaa myös säätimeen, jolla valitaan,
  milloin Windows käynnistetään uudelleen päivitysten asentamisen
  viimeistelemiseksi.

## Laskin

* NVDA ilmoittaa laskutoimituksen tuloksen Enteriä tai Esciä painettaessa.
* NVDA puhuu laskutoimitusten tulokset (esim. yksikkö- ja
  valuuttamuuntimessa) heti laskukaavoja syötettäessä.

## Kalenteri

* NVDA ei sano enää "muokattava" tai "vain luku" viestisisällössä ja muissa
  kentissä.

## Cortana

* Cortanan tekstimuotoiset vastaukset puhutaan useimmissa tilanteissa
  (mikäli näin ei ole, avaa Käynnistä-valikko uudelleen ja yritä hakua
  toistamiseen).
* NVDA on hiljaa puhuessasi Cortanalle mikrofonin välityksellä.
* NVDA puhuu nyt vahvistuksen muistutusta lisättäessä.

## Pelipalkki

* NVDA ilmoittaa pelipalkki-ikkunan ilmestymisestä. Teknisistä rajoituksista
  johtuen NVDA ei voi olla täysin vuorovaikutuksessa pelipalkin kanssa.

## Groove Music

* Ehdotusten ilmestyminen havaitaan nyt kappaleita etsittäessä.

## Sähköposti

* Voit nyt käyttää viestiluettelon kohteita tarkastellessasi
  taulukkonavigointikomentoja viestiotsakkeiden lukemiseen.
* Ät-maininnan ehdotukset ilmaistaan äänimerkeillä viestiä kirjoitettaessa.

## Kartat

* NVDA soittaa äänimerkin karttasijainneille.
* NVDA ilmoittaa katuosoitteet käyttäessäsi nuolinäppäimiä kartalla
  liikkumiseen oltaessa street side -näkymässä ja mikäli "use keyboard"
  -vaihtoehto on otettu käyttöön.

## Microsoft Edge

* Ilmoitukset, kuten tiedostojen lataukset ja useat verkkosivujen
  ilmoitukset, luetaan. Suurin osa näistä muutoksista sisältyy NVDA
  2017.3:een.

## Ihmiset

* Kontakteja etsittäessä toistetaan ääni, mikäli hakutuloksia on.

## Asetukset

* Määrätyt tiedot, kuten Windows Updaten päivitysten asennuksen edistyminen,
  puhutaan nyt automaattisesti. NVDA 2017.3 käsittelee itse useimmat näistä
  tapauksista.
* Edistymispalkkien arvoja tai muita tietoja ei lueta enää kahdesti.
* Mikäli asetusten etsiminen kestää jonkin aikaa, NVDA ilmoittaa "etsitään"
  sekä hakutulosten tilan, kuten sen, jos asetusta ei löydy. Tämä muutos
  sisältyy NVDA 2017.3:een.
* Asetusryhmät tunnistetaan säätimien välillä liikuttaessa
  objektinavigointia käyttäen.
* NVDA ei enää epäonnistu joidenkin yhdistelmäruutujen selitteiden
  tunnistamisessa ja/tai arvomuutosten ilmoittamisessa. Arvomuutosten
  korjaus sisältyy NVDA 2017.3:een.

## Skype

* Kirjoitusilmaisimen teksti puhutaan kuten Skypen työpöytäversiossa.
* Osittainen Control+NVDA+numero-komentojen paluu tuoreen
  keskusteluhistorian lukemiseen sekä navigointiobjektin siirtämiseen
  keskustelukohteisiin kuten Skypen työpöytäversiossa.
* Voit nyt painaa Alt+numerorivin numeroita etsiäksesi kontaktiluettelon
  (1), keskustelut (2), botit (3) ja keskustelumuokkauskentän, mikäli se on
  näkyvissä (4) sekä siirtyäksesi niihin. Huomaa, että nämä komennot
  toimivat oikein, jos maaliskuussa 2017 julkistettu Skype-päivitys on
  asennettu.
* Marraskuussa 2016 julkaistun Skype-sovelluksen esiversion
  yhdistelmäruutujen selitteet puhutaan.
* NVDA ei enää sano "Skype-viesti" useimmissa tapauksissa viestejä
  tarkasteltaessa.
* Korjattu useita ongelmia, joita ilmeni käytettäessä Skypeä pistenäytön
  kanssa, mukaan lukien kyvyttömyys lukea viestihistorian kohteita
  pistekirjoituksella.
* NVDA kertoo nyt viestin tarkat tiedot, kuten kanavatyypin ja
  lähetyspäivämäärän sekä -kellonajan jne., painettaessa NVDA+D
  viestihistorialuettelon kohteen kohdalla.

## Kauppa

* Sovellusten nimet näytetään oikein päivitettävien sovellusten luettelossa
  päivitystarkistuksen jälkeen.
* Hakutulosehdotusten ilmestyminen ilmoitetaan. Tämä sisältyy NVDA
  2017.3:een.
* NVDA ilmoittaa tuotteen nimen ja latauksen edistymisen sisältöä, kuten
  sovelluksia ja elokuvia, ladattaessa. Peruskorjaus sisältyy NVDA
  2017.3:een.

## Sää

* Sellaiset välilehdet kuten "ennuste" ja "kartat" tunnistetaan oikeiksi
  välilehdiksi (korjauksen tehnyt Derek Riemer).
* Käytä ennustetta lukiessasi vasenta ja oikeaa nuolta kohteiden välillä
  liikkumiseen. Käytä nuolta ylös ja alas yksittäisten kohteiden
  lukemiseen. Esim.  oikeaa nuolta painettaessa saatetaan sanoa "Maanantai:
  26,1 astetta, puolipilvistä, ...", ja nuolta alas painettaessa
  "Maanantai". Uudelleen painaminen lukee seuraavan kohteen (kuten
  lämpötilan). Toimii tällä hetkellä päivittäisiin ja tunnin välein
  tehtäviin ennusteisiin.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=w10

[2]: https://addons.nvda-project.org/files/get.php?file=w10-dev
