import json

data = [
{
"name": "Leerstein: Magie annulieren",
"cost_silver": 0,
"cost_zynalith": 1,
"victory_points": 0,
"description": "Konter: Verhindere das Ausspielen einer Magie-Karte, nachdem sie bezahlt wurde. Sie wird zerstört. Der andere Spieler erhält diese \"Leerstein: Magie annulieren\"-Karte auf die Hand.",
"image": "void_stone"
},
{
"name": "Zurück zum Alltag",
"cost_silver": 2,
"cost_zynalith": 0,
"victory_points": 0,
"description": "Konter: Verhindere ein Event. Es wird zerstört.",
"image": "mill"
},
{
"name": "Versteck",
"cost_silver": 2,
"cost_zynalith": 0,
"victory_points": 0,
"description": "Konter: Verhindere eine Schadensaktion an dir.",
"image": "hut"
},
]

with open("../card_data/interrupts", "w") as f:
    f.write(json.dumps(data))
