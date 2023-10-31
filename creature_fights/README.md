Start: Jeder Spieler startet mit 20 HP für sich selbst.


Es gibt 5 Runden mit wechselndem Startspieler im Uhrzeigersinn mit je einer Hauptaktion. Zu Beginn einer jeden Runde erhält jeder Spieler 10 Silber.
Jeder Spieler kann normalerweise maximal 5 Wesen ausgespielt haben.
Jede Runde wird die Auslage refresht:
Es gibt einen Stapel mit Wesen (und Wesen-Events).
Es gibt einen Stapel mit Zusatzkarten und Zusatz-Events.
Von beiden Stapeln werden 5 gezogen und als Auslage bereitgehalten.
Sobald Events gezogen werden, werden dieses sofort ausgeführt.

Hauptaktionen je Zug innerhalb einer Runde:
- Karte für 1s von Auslage auf Hand nehmen
- Karte aus Hand oder Auslage bezahlen und ausspielen
- Eigenes Wesen aus Front verbannen und Kosten zurückerhalten (nicht die Kosten von Zusatzkarten)
- Passen für diese Runde

Nebenaktionen:
- Position von eigenen Wesen vertauschen, welche selben INIT-Wert besitzen
- Konter ausspielen (von der Hand oder Auslage)

Zusatzkarten:
- Buffs/Eigenschaften
- Zauber/Magie
- Gegenstände/Ausrüstung

All diese Karten können nicht mehr ausgetauscht werden bei einem Wesen.


Sieg und Spielende:
Falls nur ein Spieler lebt (>=1 HP), gewinnt dieser.
Ansonsten werden 5 Runden gespielt und es gewinnt der von den noch lebenden Spielern mit den meisten Siegpunkten := aufgedruckte VP + Zynalith-Besitz + Silber/10 (abgerundet)


Kampf:
Die Wesen müssen in Reihenfolge der INIT-Werte platziert werden (Die Zahl nach Effekten zählt).
Absteigend dieser Reihenfolge, schickt jeder Spieler ein Wesen in den Kampf. Diese Kampf-Linie wertet aus, wer den Kampf für sich entscheidet: Das Wesen mit dem höchsten ATK-Wert. Anschließend verlieren alle weiteren Wesen diesen Wert an HP (minus ihres DEF-Wertes). Bei 0 HP sterben sie. Überschüssiger Schaden wird an den Spieler weitergeleitet.
Beispiel: Es gewinnt ein Wesen in der Linie mit 3 ATK. Ein anderes Wesen der Linie hat 1 DEF und 1 verbleibendes HP (Marker auf der Karte). Es erhält 3-1=2 Schaden. Verliert das letzte HP, wird zerstört und den verbleibenden 1 Schadenspunkt erhält der Spieler, welcher zudem auch die Kosten des Wesens zurückerhält.
Wenn ein Wesen zerstört wird, erhält der Spieler die Kosten des Wesens zurück (aber nicht er Zusatzkarten).

Keywords für Triggerzeitpunkt:
- Sofort: sofort
- Kampf: in jeder Kampfrunde (auch Sturmangriff), in dem es mindestens einen Gegner in der Linie gibt; Innerhalb einer Linie wird in folgender Reihe abgearbeitet: INIT-Reihenfolge > ATK-Wert > DEF-Wert > Verbleibende HP > Schere-Stein-Papier
Keywords für Effekt:
- Sturmangriff: Zusätzliche spontane Kampfrunde nur für diese Linie
- Blutsaugen: Schaden, den dieses Wesen an gegnerischen Helden verursacht, heilt es den eigenen Helden





Offene Ideen:
- Zwei Fronten
- Gesichtsloser Krieger 0/?/?/?, 1VP, 15Silber (erhält Werte des Wesens links neben diesem (ohne Zusatzkarten))
- Für jeden Sieg in einer Linie, erhält der Gewinner 1 Zynalith (too strong?)