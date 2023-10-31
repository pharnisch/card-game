import json

data = [
{
"name": "Glückliche Fügung",
"cost_silver": 0,
"cost_zynalith": 1,
"victory_points": 0,
"type": "spell",
"description": "Sofort: Erhalte 3 Zynalith."
},
{
"name": "Aderlass",
"cost_silver": 0,
"cost_zynalith": 1,
"victory_points": 0,
"type": "spell",
"description": "Kampf: -1 HP (Spieler oder dieses Wesen) und erhalte 1 Zynalith."
},




{
"name": "Fernrohr",
"cost_silver": 0,
"cost_zynalith": 0,
"victory_points": 0,
"type": "equipment",
"description": "Sofort: Ziehe eine Karte."
},
{
"name": "Minenwerkzeug",
"cost_silver": 3,
"cost_zynalith": 0,
"victory_points": 0,
"type": "equipment",
"description": "Kampf: Erhalte 1 Zynalith."
},
{
"name": "Lupe",
"cost_silver": 0,
"cost_zynalith": 0,
"victory_points": 0,
"type": "equipment",
"description": "Sofort: Erhalte 1 Zynalith."
},
{
"name": "Banner",
"cost_silver": 2,
"cost_zynalith": 0,
"victory_points": 0,
"type": "equipment",
"description": "Sofort: Sturmangriff."
},
{
"name": "Rostige Klinge",
"cost_silver": 3,
"cost_zynalith": 0,
"victory_points": 0,
"type": "equipment",
"description": "Kampf: Gegnerwesen in Linie verlieren 1 HP."
},
{
"name": "Krone",
"cost_silver": 3,
"cost_zynalith": 0,
"victory_points": 3,
"type": "equipment",
"description": ""
},
]

with open("../card_data/equipment_and_spells", "w") as f:
    f.write(json.dumps(data))
