# Import nach Home Assistant

## Blueprint

```text
cp home-assistant/blueprints/automation/bkw_effizienz_steigern/nulleinspeisung_2wr.yaml \
  /config/blueprints/automation/bkw_effizienz_steigern/nulleinspeisung_2wr.yaml
```

Danach Home Assistant neu laden und Automation aus Blueprint erstellen.

## Custom Component

```text
cp -r custom_components/bkw_effizienz_steigern /config/custom_components/
```

Home Assistant neu starten. Danach steht der Service zur Verfuegung:

```text
bkw_effizienz_steigern.calculate_setpoints
```
