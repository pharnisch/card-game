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
"name": "Gedankenkontrolle",
"cost_silver": 0,
"cost_zynalith": 3,
"victory_points": 0,
"type": "spell",
"description": "Sofort: Übernehme die Kontrolle über ein gegnerisches Wesen."
},
{
"name": "Reinigung",
"cost_silver": 0,
"cost_zynalith": 2,
"victory_points": 0,
"type": "spell",
"description": "Kampf: Zerstöre eine Eigenschafts-Karte von einem gegnerischen Wesen."
},
{
"name": "Massenbannung",
"cost_silver": 0,
"cost_zynalith": 1,
"victory_points": 0,
"type": "spell",
"description": "Sofort: Alle Eigenschafts-Karten aller Spieler gehen auf die Hand ihres Besitzers zurück."
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
"cost_silver": 5,
"cost_zynalith": 0,
"victory_points": 1,
"type": "equipment",
"description": "Kampf: Gegnerwesen der Linie verlieren 1 HP."
},
{
"name": "Krone",
"cost_silver": 3,
"cost_zynalith": 0,
"victory_points": 3,
"type": "equipment",
"description": ""
},
{
"name": "Brüchiger Talisman des Schutzes",
"cost_silver": 2,
"cost_zynalith": 0,
"victory_points": 0,
"type": "equipment",
"description": "Kampf: Falls dieses Wesen einen Kampf verlieren sollte, erhältst du in diesem Kampf keinen Schaden - zerstöre dann außerdem diese Ausrüstungskarte."
},
{
"name": "Schurken-Rucksack",
"cost_silver": 4,
"cost_zynalith": 0,
"victory_points": 0,
"type": "equipment",
"description": "Sofort: Lege eine Ausrüstungskarte von einem gegnerischen Wesen unter ein eigenes."
},
{
"name": "Giftphiole",
"cost_silver": 7,
"cost_zynalith": 0,
"victory_points": 0,
"type": "equipment",
"description": "Sofort: Zerstöre ein Wesen mit ATK-Wert >= 7 (insgesamt)."
},
]

with open("../card_data/equipment_and_spells", "w") as f:
    f.write(json.dumps(data))
