import json

data = [
{
"name": "Leerstein: Magie annulieren",
"cost_silver": 0,
"cost_zynalith": 1,
"victory_points": 0,
"description": "Konter: Verhindere das Ausspielen einer Magie-Karte, nachdem sie bezahlt wurde. Sie wird zerstört."
},
{
"name": "Zurück zum Alltag",
"cost_silver": 2,
"cost_zynalith": 0,
"victory_points": 0,
"description": "Konter: Verhindere ein Event. Es wird zerstört."
},
{
"name": "Versteck",
"cost_silver": 2,
"cost_zynalith": 0,
"victory_points": 0,
"description": "Konter: Verhindere eine Schadensaktion an dir."
},
]

with open("../card_data/interrupts", "w") as f:
    f.write(json.dumps(data))
