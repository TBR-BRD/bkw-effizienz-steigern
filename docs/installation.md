# Installation

## Reihenfolge

1. Repo clonen oder ZIP entpacken.
2. Diagramm und Hardwareliste an konkrete Anlage anpassen.
3. AC- und DC-Schutzkonzept mit Elektrofachkraft pruefen.
4. Messgeraet am Hausanschluss integrieren.
5. Wechselrichter und MPPT in Home Assistant einbinden.
6. Blueprint importieren und Entitaeten zuordnen.
7. Mit niedriger Leistung testen.
8. Logging aktivieren und Regelparameter nachjustieren.

## GitHub Upload

```bash
git init
git remote add origin https://github.com/TBR-BRD/bkw-effizienz-steigern.git
git add .
git commit -m "Initial commit: BKW Effizienzsteigerung"
git branch -M main
git push -u origin main
```

## Home Assistant

Siehe [home-assistant.md](home-assistant.md).

## Inbetriebnahme-Test

1. WR1 und WR2 auf 0 W begrenzen.
2. Messgeraet-Vorzeichen pruefen: Bezug muss positiv sein.
3. WR1 manuell auf 50 W setzen und Zaehlerreaktion pruefen.
4. WR1 auf 100 W setzen und Zaehlerreaktion pruefen.
5. WR2 mit kleiner Zusatzleistung testen.
6. Automatik einschalten.
7. Zielwert `+15 W` und Deadband `8 W` verwenden.
8. Log pruefen: Keine dauerhafte Rueckeinspeisung, keine Schwingung.
