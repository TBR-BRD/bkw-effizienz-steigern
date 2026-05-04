# Security Policy

Bitte melde Sicherheitsprobleme nicht als oeffentliches Issue, wenn sie reale Anlagen gefaehrden koennen.

Typische sensible Daten:

- Home-Assistant-Token
- MQTT-Zugangsdaten
- WLAN-Zugangsdaten
- lokale IP-Adressen, wenn sie nicht veroeffentlicht werden sollen
- Seriennummern von Zaehlern und Wechselrichtern

Der Code in diesem Repository ist fail-safe ausgelegt: Wenn Messgeraet, Akku oder Regler nicht plausibel sind, sollen die Wechselrichter abgeschaltet oder auf 0 W begrenzt werden.
