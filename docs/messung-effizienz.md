# Effizienzmessung und Motivation

Der technische Grund fuer dieses Projekt sind hohe Teillastverluste von Batteriewechselrichtern.

In einem c't-Labortest des Growatt Nexa 2000 wurde unter anderem gemessen:

- ca. 50 W Grundverbrauch schon ohne AC-Verbraucher,
- 32 % Wirkungsgrad bei 25 W Ausgangsleistung,
- knapp 59 % Wirkungsgrad bei 75 W,
- ueber 80 % ab etwa 200 W,
- 86 % bei 500 W.

Die Tendenz ist typisch: Wechselrichter arbeiten meist in der Naehe ihres passenden Leistungsbereichs effizienter als bei sehr niedriger Last. Deshalb wird hier eine kleine Grundlaststufe mit 100 VA und eine zweite Zusatzstufe mit 600 VA kombiniert.

## Eigene Messung

Minimaler Messaufbau:

1. Energie in den Akku bzw. Speicher messen.
2. Abgegebene AC-Energie messen.
3. Round-Trip-Efficiency berechnen.

```text
Wirkungsgrad [%] = abgegebene Energie / eingespeicherte Energie * 100
```

Fuer die Optimierung des Grundlastbetriebs ist eine Nachtmessung sinnvoll:

```text
Grundlast [W] = Energieverbrauch Nacht [Wh] / Nachtstunden [h]
```

## Warum 12 V DC?

Router, ONT, kleine Switches und Sensorik nutzen intern DC. Ein DC/DC-Wandler vom 48-V-Akku auf 12 V vermeidet den ineffizienten Weg:

```text
Akku DC -> 230 V AC -> Steckernetzteil -> 12 V DC
```
