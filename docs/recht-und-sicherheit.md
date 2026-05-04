# Recht und Sicherheit in Deutschland

Stand: 2026-05-04. Bitte vor Aufbau/Inbetriebnahme erneut pruefen.

## Leistungsgrenzen Steckersolar

Fuer steckerfertige Solaranlagen bzw. Steckersolargeraete wird im Marktstammdatenregister die Grenze mit maximal 2.000 W installierter Leistung und maximal 800 W/VA Wechselrichterleistung beschrieben.

Projekt-Auslegung:

```text
PV:  bis 2.000 Wp
WR1: 100 VA
WR2: 600 VA
Summe: 700 VA
Reserve zur 800-VA-Grenze: 100 VA
```

## Maximal waehlebare Wechselrichterleistung

Wichtig: Bei Geraeten mit per Software oder App waehbarer Leistung ist fuer die Steckersolar-Sonderregeln die maximal waehlebare Wechselrichterleistung relevant. Ein 900-VA-Geraet, das nur auf 600 VA eingestellt wird, ist deshalb nicht automatisch ein 600-VA-Steckersolargeraet.

## Anschlussart

Bei Haushaltsstecker/Schuko gelten technische Zusatzanforderungen. Der VDE beschreibt fuer Haushaltsstecker eine niedrigere zulaessige Modulleistung von 960 Wp; fuer bis 2.000 Wp ist eine spezielle Energiesteckvorrichtung die sichere Option.

## Speicher

Fuer den DC-Akku gibt es in den Steckersolar-Leistungsgrenzen keine einfache feste kWh-Obergrenze. Batteriespeicher sind aber im Marktstammdatenregister zu betrachten bzw. zu registrieren. Bei Solaranlagen mit Batteriespeichern koennen zwei Einheiten zu registrieren sein.

## Sicherheit

- AC-Arbeiten nur durch Elektrofachkraft.
- Keine Mehrfachsteckdose fuer mehrere Erzeugungsanlagen verwenden.
- DC-Seite mit passenden Sicherungen, Trennstellen, Leitungsquerschnitten und Brandlastbewertung planen.
- BMS-Grenzen fuer Strom, Spannung und Temperatur beachten.
- Wechselrichter nur einsetzen, wenn sie fuer netzparallelen Betrieb geeignet sind.
- Keine unsynchronisierte Parallelschaltung von Inselwechselrichtern mit dem Hausnetz.

## Offizielle Quellen

- Bundesnetzagentur: Balkon-Solaranlagen und Steckersolargeraete: https://www.bundesnetzagentur.de/DE/Fachthemen/ElektrizitaetundGas/ErneuerbareEnergien/Solaranlagen/Balkon_table.html
- Marktstammdatenregister, Arten der Solaranlagen: https://www.marktstammdatenregister.de/MaStRHilfe/files/regHilfen/Arten_der_Solaranlagen_im_Marktstammdatenregister_%E2%80%93_Uebersicht_und_Definitionen.pdf
- VDE/FNN, steckerfertige PV-Anlagen: https://www.vde.com/de/fnn/themen/tar/tar-niederspannung/erzeugungsanlagen-steckdose
- MaStR Registrierung mit Batteriespeichern: https://www.marktstammdatenregister.de/MaStRHilfe/subpages/regCheckSolar.html
