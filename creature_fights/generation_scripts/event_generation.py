import json

data = [
{
"name": "Goblin-Diplomat",
"description": "Am Ende dieser Runde findet kein Kampf statt.",
"image": "goblin_diplomat"
},
{
"name": "Elfen-Fürst",
"description": "Alle Spieler ohne Zynalith, erhalten 1 Zynalith.",
"image": "elfen_fuerst"
},
{
"name": "Menschen-König",
"description": "Alle Spieler mit mindestens 5 Silber, erhalten 3 Silber.",
"image": "menschen_koenig"
},
{
"name": "Bettler",
"description": "Alle mit mindestens einem Silber werfen eines ab.",
"image": "hands_full_of_silver"
},
{
"name": "Instabiles Naturphänomen",
"description": "Alle Helden erhalten so viel Schaden wie sie an Zynalith besitzen.",
"image": "magic_storm"
},
{
"name": "Rost",
"description": "Das/die Wesen mit dem höchsten ATK-Wert wird zerstört.",
"image": "rost"
},
{
"name": "Zeitkrümmung",
"description": "Alle Sofort-Effekte können erneut ausgeführt werden, beginnend beim aktiven Spieler, in beliebiger Reihenfolge unabhängig vom INIT-Wert.",
"image": "zeitkruemmung"
},
{
"name": "Elfen-Dynastie Brinth",
"description": "Alle Spieler ziehen drei Karten vom Zusatz-Karten-Stapel.",
"image": "elfen_stadt_briam"
},
{
"name": "Untergang der Zivilisationen",
"description": "Es findet eine spontane zusätzliche Kampfrunde statt.",
"image": "verzauberte_gebaeude"
}
]

with open("../card_data/events", "w") as f:
    f.write(json.dumps(data))
