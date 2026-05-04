# Regelalgorithmus

## Vorzeichenkonvention

```text
P_grid > 0 W  = Bezug aus dem Netz
P_grid < 0 W  = Einspeisung ins Netz
```

## Zielwert

Das System regelt nicht exakt auf 0 W, sondern auf einen kleinen positiven Netzbezug:

```text
P_grid_target = +15 W
```

Dadurch bleibt eine Reserve gegen Messrauschen, Latenz und Lastspruenge.

## Grundformel

```text
P_total_next = P_total_current + P_grid - P_grid_target
P_total_next = begrenzen auf 0 ... 700 W
```

Die 700 W ergeben sich aus:

```text
WR1 100 W + WR2 600 W = 700 W
```

Die rechtliche Obergrenze von 800 VA wird zusaetzlich als harte Grenze im Code gefuehrt.

## Verteilung auf die Wechselrichter

```text
wenn P_total_next < 50 W:
    WR1 = 0 W
    WR2 = 0 W

wenn 50 W <= P_total_next <= 100 W:
    WR1 = P_total_next
    WR2 = 0 W

wenn P_total_next > 100 W:
    WR1 = 100 W
    WR2 = P_total_next - 100 W, maximal 600 W
```

Zur Effizienzsteigerung kann WR2 bei sehr kleinen Sollwerten unterhalb seines effizienten Bereichs ausgeschaltet bleiben. Dann wird ein kleiner Netzbezug akzeptiert.

## Sicherheitsregeln

Der Regler soll fail-safe arbeiten:

- Messgeraet offline: WR1 = 0 W, WR2 = 0 W.
- Akku-SOC unter Stop-Schwelle: WR1 = 0 W, WR2 = 0 W.
- Akku nicht plausibel oder BMS-Fehler: WR1 = 0 W, WR2 = 0 W.
- WR-Summe nie ueber installierter Leistung und nie ueber 800 VA.
- Positiver Netzbezug als Zielwert statt aggressiver Rueckeinspeisung.

## Python-Beispiel

```python
from bkw_effizienz_steigern.controller import ControllerConfig, ControllerInput, calculate_setpoints

cfg = ControllerConfig()
inp = ControllerInput(
    grid_power_w=480,
    wr1_actual_w=100,
    wr2_actual_w=200,
    battery_soc_pct=65,
)
print(calculate_setpoints(inp, cfg))
```
