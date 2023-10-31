import json

data = [
{
"name": "Goblin-Diplomat",
"description": "Am Ende dieser Runde findet kein Kampf statt."
},
{
"name": "Elfen-Fürst",
"description": "Alle Spieler ohne Zynalith, erhalten 1 Zynalith."
},
{
"name": "Menschen-König",
"description": "Alle Spieler mit mindestens 5 Silber, erhalten 3 Silber."
},
{
"name": "Bettler",
"description": "Alle mit mindestens einem Silber geben eines ab."
},
{
"name": "Instabiles Naturphänomen",
"description": "Alle Helden erhalten so viel Schaden wie sie an Zynalith besitzen."
},
{
"name": "Rost",
"description": "Das/die Wesen mit dem höchsten ATK-Wert wird zerstört."
},
{
"name": "Zeitkrümmung",
"description": "Alle Sofort-Effekte können erneut ausgeführt werden, beginnend beim aktiven Spieler, in beliebiger Reihenfolge unabhängig vom INIT-Wert."
}
]

with open("../card_data/events", "w") as f:
    f.write(json.dumps(data))