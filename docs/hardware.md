# Hardware

Die Einkaufsliste befindet sich in:

- [hardware/bom.csv](../hardware/bom.csv)
- [hardware/bom.md](../hardware/bom.md)
- [hardware/BKW_Hardwareliste_Einkauf_2WR_2000Wp.xlsx](../hardware/BKW_Hardwareliste_Einkauf_2WR_2000Wp.xlsx)

## Kritischer Punkt: WR1 mit echter 100-VA-Grenze

Ein echter netzparalleler 100-VA-Wechselrichter ist schwerer zu finden als uebliche 300- bis 800-VA-Mikrowechselrichter. Fuer die saubere Umsetzung sollte WR1 auf Typenschild, Zertifikat oder Herstellerbestaetigung maximal 100 VA ausweisen.

Nicht gleichwertig ist ein groesserer Wechselrichter, der nur per Software auf 100 W gedrosselt wird, wenn die maximal waehlebare Leistung hoeher ist.

## Alternative mit Serienware

Wenn kein echter 100-VA-WR verfuegbar ist, ist technisch und organisatorisch oft einfacher:

```text
WR1: 300 VA
WR2: 500 VA
Summe: 800 VA
```

Der 300-VA-WR kann dann per Regelung im Bereich 50 bis 100 W gefahren werden. Rechtlich ist dann aber 300 VA seine Wechselrichterleistung, nicht 100 VA.

## Akku-Auswahl

Empfohlen wird ein 48-V-/51,2-V-LiFePO4-System mit BMS. Die Beispiel-BOM nutzt 4,8 kWh als praxisnahen Startpunkt. Groessere Speicher koennen technisch moeglich sein, muessen aber fachgerecht geplant und registriert werden.
