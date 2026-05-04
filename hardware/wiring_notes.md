# Verdrahtungsnotizen

## DC-Seite

- PV-Strings passend zum MPPT-Spannungsfenster planen.
- Leerlaufspannung bei tiefster Temperatur beachten.
- DC-Trennstelle, Stringschutz und Ueberspannungsschutz vorsehen.
- Akku mit passender Hauptsicherung, Hauptschalter und BMS-Freigabe anschliessen.
- WR1 und WR2 ueber getrennte Sicherungen und optional DC-Schuetze versorgen.
- DC/DC-Wandler fuer 12 V getrennt absichern.

## AC-Seite

- WR1 und WR2 nur netzparallel betreiben, wenn sie dafuer zugelassen sind.
- AC-seitige Zusammenfuehrung, RCD, LS und Ueberspannungsschutz objektbezogen planen.
- Keine Mehrfachsteckdose fuer mehrere Erzeugungsanlagen verwenden.
- Messgeraet am Hausanschluss so einbauen, dass es Bezug und Einspeisung korrekt erkennt.

## Vorzeichenpruefung

Vor der Automatik:

```text
Wasserkocher einschalten -> P_grid muss positiver werden.
PV/WR einschalten       -> P_grid muss kleiner werden.
```
