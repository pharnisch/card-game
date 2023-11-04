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
"name": "Zerquetschen",
"cost_silver": 0,
"cost_zynalith": 2,
"victory_points": 0,
"type": "spell",
"description": "Sofort: Zerstöre von ALLEN Spielern die zwei äußersten Wesen."
},
{
"name": "Opfer-Ritual",
"cost_silver": 0,
"cost_zynalith": 2,
"victory_points": 0,
"type": "spell",
"description": "Sofort: Zerstöre ein eigenes Wesen und erhalte die doppelten Kosten zurück."
},
{
"name": "Kometen-Hagel",
"cost_silver": 0,
"cost_zynalith": 2,
"victory_points": 1,
"type": "spell",
"description": "Kampf: Wirf beliebig viele Karten von deiner Hand ab und verursache allen Mitspielern Schaden entsprechend der Anzahl."
},
{
"name": "Schutz-Zauber",
"cost_silver": 0,
"cost_zynalith": 2,
"victory_points": 0,
"type": "spell",
"description": "Passiv: Dieses Wesen kann immer nur jeweils 1 Schaden erleiden."
},
{
"name": "Feuerball",
"cost_silver": 0,
"cost_zynalith": 1,
"victory_points": 0,
"type": "spell",
"description": "Sofort: Füge einem Spieler 4 Schaden zu."
},
{
"name": "Funke",
"cost_silver": 0,
"cost_zynalith": 1,
"victory_points": 0,
"type": "spell",
"description": "Kampf: Füge einem Spieler oder Wesen 1 Schaden zu."
},
{
"name": "Verjüngung",
"cost_silver": 0,
"cost_zynalith": 1,
"victory_points": 0,
"type": "spell",
"description": "Kampf: Heile einen Spieler oder Wesen um 1 HP."
},
{
"name": "Erdbeben",
"cost_silver": 0,
"cost_zynalith": 4,
"victory_points": 2,
"type": "spell",
"description": "Spielende: Füge ALLEN Spielern 8 Schaden zu."
},
{
"name": "Ausgeglichene Magie",
"cost_silver": 0,
"cost_zynalith": 4,
"victory_points": 3,
"type": "spell",
"description": "Sofort: Setze alle Spieler auf 15 HP."
},
{
"name": "Federleichter Flug",
"cost_silver": 0,
"cost_zynalith": 0,
"victory_points": 0,
"type": "spell",
"description": "Sofort: Gebe ein Wesen auf die Hand des Spielers zurück samt Zusatzkarten, er erhält aber nur die Kosten des Wesens erstattet."
},
{
"name": "Heilender Nebel",
"cost_silver": 0,
"cost_zynalith": 1,
"victory_points": 0,
"type": "spell",
"description": "Kampf: Heile die beiden Wesen neben diesem um 1."
},
{
"name": "Dimensionsriss",
"cost_silver": 0,
"cost_zynalith": 4,
"victory_points": 3,
"type": "spell",
"description": "Spielende: Erhalte so viel Zynalith wie du an Magiewesen besitzt."
},
{
"name": "Endloses Leben",
"cost_silver": 0,
"cost_zynalith": 5,
"victory_points": 0,
"type": "spell",
"description": "Tod: Ersetze dieses Wesen mit dem nächsten Wesen des Nachziehstapels. Übernehme alle vorherigen Zusatzkarten, inklusive diesem Zauber."
},
{
"name": "Wandelnder Kristall",
"cost_silver": 0,
"cost_zynalith": 5,
"victory_points": 0,
"type": "spell",
"description": "Tod: Erhalte 10 Zynalith."
},
{
"name": "Arkaner Sturm",
"cost_silver": 0,
"cost_zynalith": 1,
"victory_points": 0,
"type": "spell",
"description": "Sofort: Alle müssen Karten abwerfen sodass sie maximal noch 2 Karten auf der Hand haben."
},
{
"name": "Apokalypse",
"cost_silver": 0,
"cost_zynalith": 2,
"victory_points": 0,
"type": "spell",
"description": "Passiv: Das Spiel endet nach der 4. Runde."
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
"name": "Wunschbrunnen",
"cost_silver": 4,
"cost_zynalith": 0,
"victory_points": 1,
"type": "equipment",
"description": "Kampf: Ziehe eine Karte."
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
"cost_silver": 3,
"cost_zynalith": 0,
"victory_points": 0,
"type": "equipment",
"description": "Sofort: Zerstöre ein Wesen mit ATK-Wert >= 7 (insgesamt)."
},
{
"name": "Erste-Hilfe-Set",
"cost_silver": 5,
"cost_zynalith": 0,
"victory_points": 0,
"type": "equipment",
"description": "Kampf: Heile dieses Wesen voll."
},
{
"name": "Poesie-Band",
"cost_silver": 12,
"cost_zynalith": 0,
"victory_points": 2,
"type": "equipment",
"description": "Spielende: Erhalte so viel Zynalith wie verbleibende HP auf diesem Wesen sind."
},
{
"name": "Kleine Landkarte",
"cost_silver": 3,
"cost_zynalith": 0,
"victory_points": 2,
"type": "equipment",
"description": "Passiv: Du kannst auch die Position deiner Wesen mit einem INIT-Unterschied von bis zu 1 vertauschen."
},
{
"name": "Große Landkarte",
"cost_silver": 6,
"cost_zynalith": 0,
"victory_points": 2,
"type": "equipment",
"description": "Passiv: Du kannst auch die Position deiner Wesen mit einem INIT-Unterschied von bis zu 2 vertauschen."
},
{
"name": "Gezinkte Würfel",
"cost_silver": 4,
"cost_zynalith": 0,
"victory_points": 0,
"type": "equipment",
"description": "Sofort: Vertausche von zwei Wesen die Magiekarten mit selben Kosten."
},
{
"name": "Diplomatie-Urkunde",
"cost_silver": 0,
"cost_zynalith": 0,
"victory_points": 1,
"type": "equipment",
"description": "Sofort: Gebe allen Mitspielern 3 Silber von dir, danach heilen sich alle Spieler voll."
},
{
"name": "Trauer-Kasse",
"cost_silver": 4,
"cost_zynalith": 0,
"victory_points": 1,
"type": "equipment",
"description": "Trauer: Erhalte 2 Silber."
},
{
"name": "Gewürze",
"cost_silver": 3,
"cost_zynalith": 0,
"victory_points": 0,
"type": "equipment",
"description": "Trauer: Heile die HP von dir oder diesem Wesen um 2."
},
{
"name": "Spurt-Sandalen",
"cost_silver": 1,
"cost_zynalith": 0,
"victory_points": 0,
"type": "equipment",
"description": "Passiv: Du kannst pro Zug 1 bis 2 Hauptaktionen durchführen."
},
{
"name": "Grab-Schaufel",
"cost_silver": 0,
"cost_zynalith": 0,
"victory_points": 0,
"type": "equipment",
"description": "Trauer: Ziehe eine Karte."
},
{
"name": "Leiser Dolch",
"cost_silver": 4,
"cost_zynalith": 0,
"victory_points": 0,
"type": "equipment",
"description": "Trauer: Erhalte 1 Zynalith."
},
{
"name": "Kriegserklärung",
"cost_silver": 5,
"cost_zynalith": 0,
"victory_points": 0,
"type": "equipment",
"description": "Passiv: Es gibt eine zusätzliche 6. Runde (außer bei einer Apokalypse)."
},
]

with open("../card_data/equipment_and_spells", "w") as f:
    f.write(json.dumps(data))
