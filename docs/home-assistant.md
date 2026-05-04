# Home Assistant

Dieses Repository enthaelt drei Bausteine:

1. Blueprint fuer die eigentliche Nulleinspeisungsregelung.
2. Beispiel-Dashboard fuer Monitoring.
3. HACS-faehige Custom Integration mit Service `bkw_effizienz_steigern.calculate_setpoints` als Startpunkt fuer eigene Automationen.

## Blueprint importieren

Datei:

```text
home-assistant/blueprints/automation/bkw_effizienz_steigern/nulleinspeisung_2wr.yaml
```

Kopiere sie nach:

```text
/config/blueprints/automation/bkw_effizienz_steigern/nulleinspeisung_2wr.yaml
```

Danach Home Assistant neu laden und eine Automation aus dem Blueprint erstellen.

## Benoetigte Entitaeten

| Funktion | Beispiel |
|---|---|
| Hausanschlussleistung | `sensor.shelly_pro_3em_total_active_power` |
| Akku-SOC | `sensor.battery_soc` |
| WR1 Leistungslimit | `number.wr1_power_limit` |
| WR2 Leistungslimit | `number.wr2_power_limit` |
| WR1 Ein/Aus | `switch.wr1_enable` |
| WR2 Ein/Aus | `switch.wr2_enable` |

Die exakten Entitaeten haengen von deiner Integration ab, z. B. OpenDTU-onBattery, MQTT, Victron, Shelly oder Modbus.

## Empfohlene Startwerte

| Parameter | Wert |
|---|---:|
| Ziel-Netzbezug | 15 W |
| Deadband | 8 W |
| WR1 min | 50 W |
| WR1 max | 100 W |
| WR2 min | 50 W |
| WR2 max | 600 W |
| Installierte Grenze | 700 W |
| Rechtliche Grenze | 800 VA |
| SOC Stop | 20 % |
| SOC Resume | 25 % |

## Custom Integration

Die Custom Integration registriert einen Service, der aus Eingaben Setpoints berechnet. Sie greift nicht automatisch auf deine Wechselrichter zu; das ist bewusst so, damit die Anbindung an OpenDTU, Victron, Shelly, MQTT oder andere Systeme lokal angepasst werden kann.

Installation:

```text
custom_components/bkw_effizienz_steigern -> /config/custom_components/bkw_effizienz_steigern
```

Dann Home Assistant neu starten.
