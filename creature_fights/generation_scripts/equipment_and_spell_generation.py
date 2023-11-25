import json

data = [
{
"name": "Glückliche Fügung",
"cost_silver": 0,
"cost_zynalith": 1,
"victory_points": 0,
"type": "spell",
"description": "Sofort: Erhalte 3 Zynalith.",
"image": "magic_puzzle",
"changed": False,
},
{
"name": "Aderlass",
"cost_silver": 0,
"cost_zynalith": 1,
"victory_points": 0,
"type": "spell",
"description": "Kampf: -1 HP (Spieler oder dieses Wesen) und erhalte 1 Zynalith.",
"image": "bloody_sword"
},
{
"name": "Gedankenkontrolle",
"cost_silver": 0,
"cost_zynalith": 5,
"victory_points": 0,
"type": "spell",
"description": "Sofort: Übernehme die Kontrolle über ein gegnerisches Wesen.",
"image": "insane_human"
},
{
"name": "Reinigung",
"cost_silver": 0,
"cost_zynalith": 2,
"victory_points": 0,
"type": "spell",
"description": "Kampf: Zerstöre eine Eigenschafts-Karte von einem gegnerischen Wesen.",
"image": "beam_3"
},
{
"name": "Massenbannung",
"cost_silver": 0,
"cost_zynalith": 1,
"victory_points": 0,
"type": "spell",
"description": "Sofort: Alle Eigenschafts-Karten aller Spieler gehen auf die Hand ihres Besitzers zurück.",
"image": "beam_5"
},
{
"name": "Zerquetschen",
"cost_silver": 0,
"cost_zynalith": 2,
"victory_points": 0,
"type": "spell",
"description": "Sofort: Zerstöre von ALLEN Spielern die zwei äußersten Wesen.",
"image": "stones"
},
{
"name": "Opfer-Ritual",
"cost_silver": 0,
"cost_zynalith": 2,
"victory_points": 0,
"type": "spell",
"description": "Sofort: Zerstöre ein eigenes Wesen und erhalte die doppelten Kosten zurück.",
"image": "sacrifice"
},
{
"name": "Kometen-Hagel",
"cost_silver": 0,
"cost_zynalith": 2,
"victory_points": 1,
"type": "spell",
"description": "Kampf: Wirf beliebig viele Karten von deiner Hand ab und verursache allen Mitspielern Schaden entsprechend der Anzahl.",
"image": "fire_comets"
},
{
"name": "Schutz-Zauber",
"cost_silver": 0,
"cost_zynalith": 2,
"victory_points": 0,
"type": "spell",
"description": "Passiv: Dieses Wesen kann immer nur jeweils 1 Schaden erleiden.",
"image": "magic_shield"
},
{
"name": "Feuerball",
"cost_silver": 0,
"cost_zynalith": 1,
"victory_points": 0,
"type": "spell",
"description": "Sofort: Füge einem Spieler 4 Schaden zu.",
"image": "fireball"
},
{
"name": "Funke",
"cost_silver": 0,
"cost_zynalith": 1,
"victory_points": 0,
"type": "spell",
"description": "Kampf: Füge einem Spieler oder Wesen 1 Schaden zu.",
"image": "funke"
},
{
"name": "Verjüngung",
"cost_silver": 0,
"cost_zynalith": 1,
"victory_points": 0,
"type": "spell",
"description": "Kampf: Heile einen Spieler oder Wesen um 1 HP.",
"image": "enchanted_leaf_3"
},
{
"name": "Erdbeben",
"cost_silver": 0,
"cost_zynalith": 4,
"victory_points": 2,
"type": "spell",
"description": "Spielende: Füge ALLEN Spielern 8 Schaden zu.",
"image": "erdbeben"
},
{
"name": "Ausgeglichene Magie",
"cost_silver": 0,
"cost_zynalith": 4,
"victory_points": 3,
"type": "spell",
"description": "Sofort: Setze alle Spieler auf 15 HP.",
"image": "balanced_magic"
},
{
"name": "Federleichter Flug",
"cost_silver": 0,
"cost_zynalith": 0,
"victory_points": 0,
"type": "spell",
"description": "Sofort: Gebe ein Wesen auf die Hand des Spielers zurück samt Zusatzkarten, er erhält aber nur die Kosten des Wesens erstattet.",
"image": "magic_bird"
},
{
"name": "Heilender Nebel",
"cost_silver": 0,
"cost_zynalith": 1,
"victory_points": 0,
"type": "spell",
"description": "Kampf: Heile die beiden Wesen neben diesem um 1.",
"image": "fog_green"
},
{
"name": "Dimensionsriss",
"cost_silver": 0,
"cost_zynalith": 4,
"victory_points": 3,
"type": "spell",
"description": "Spielende: Erhalte so viel Zynalith wie du an Magiewesen besitzt.",
"image": "beam_6"
},
{
"name": "Endloses Leben",
"cost_silver": 0,
"cost_zynalith": 5,
"victory_points": 0,
"type": "spell",
"description": "Tod: Ersetze dieses Wesen mit dem nächsten Wesen des Nachziehstapels. Übernehme alle vorherigen Zusatzkarten, inklusive diesem Zauber.",
"image": "enchanted_leaf_1"
},
{
"name": "Wandelnder Kristall",
"cost_silver": 0,
"cost_zynalith": 5,
"victory_points": 0,
"type": "spell",
"description": "Tod: Erhalte 10 Zynalith.",
"image": "magic_crystal"
},
{
"name": "Arkaner Sturm",
"cost_silver": 0,
"cost_zynalith": 1,
"victory_points": 0,
"type": "spell",
"description": "Sofort: Alle müssen Karten abwerfen sodass sie maximal noch 2 Karten auf der Hand haben.",
"image": "arcane_storm"
},
{
"name": "Apokalypse",
"cost_silver": 0,
"cost_zynalith": 2,
"victory_points": 0,
"type": "spell",
"description": "Passiv: Das Spiel endet nach der 4. Runde.",
"image": "apocalypse"
},
{
"name": "Blizzard",
"cost_silver": 0,
"cost_zynalith": 2,
"victory_points": 0,
"type": "spell",
"description": "Kampf: Füge einem Spieler 3 Durchschlag-Schaden zu.",
"image": "blizzard"
},
{
"name": "Nekromantie",
"cost_silver": 0,
"cost_zynalith": 2,
"victory_points": 0,
"type": "spell",
"description": "Trauer: Heile einen Spieler oder Wesen um 3.",
"image": "necromantic1"
},
{
"name": "Seuchen-Ausbruch",
"cost_silver": 0,
"cost_zynalith": 1,
"victory_points": 0,
"type": "spell",
"description": "Trauer: ALLE Wesen erhalten 1 Schaden.",
"image": "pandemic"
},
{
"name": "Wiedergeburt",
"cost_silver": 0,
"cost_zynalith": 5,
"victory_points": 3,
"type": "spell",
"description": "Sofort: Heile einen Spieler voll.",
"image": "circle2"
},
{
"name": "Segen von Laenalith",
"cost_silver": 0,
"cost_zynalith": 6,
"victory_points": 3,
"type": "spell",
"description": "Sofort: [Sturmangriff]. Passiv: Dieses Wesen verursacht Durchschlag- und Blutsauger-Schaden.",
"image": "circle1"
},
{
"name": "Komet der Götter",
"cost_silver": 0,
"cost_zynalith": 7,
"victory_points": 1,
"type": "spell",
"description": "Sofort: Verursache 10 Schaden.",
"image": "god_comet_1"
},
{
"name": "Regen der Götter",
"cost_silver": 0,
"cost_zynalith": 3,
"victory_points": 1,
"type": "spell",
"description": "Sofort: Verursache 5 mal 1 Durchschlag-Schaden oder Heilung.",
"image": "god_rain"
},
{
"name": "Tiefgrüner Ozean: Heilende Woge",
"cost_silver": 0,
"cost_zynalith": 3,
"victory_points": 1,
"type": "spell",
"description": "Kampf: Heile alle deine Wesen und dich selbst um 3.",
"image": "green_water_whirl",
"changed": True,
},
{
"name": "Tiefgrüner Ozean: Reißender Sog",
"cost_silver": 0,
"cost_zynalith": 3,
"victory_points": 0,
"type": "spell",
"description": "Kampf: Erhalte jeweils 1 Zynalith von den anderen Spielern.",
"image": "green_water_wild",
"changed": True,
},




{
"name": "Fernrohr",
"cost_silver": 0,
"cost_zynalith": 0,
"victory_points": 0,
"type": "equipment",
"description": "Sofort: Ziehe eine Karte.",
"image": "telescope"
},
{
"name": "Wunschbrunnen",
"cost_silver": 4,
"cost_zynalith": 0,
"victory_points": 1,
"type": "equipment",
"description": "Kampf: Ziehe eine Karte.",
"image": "wishing_well"
},
{
"name": "Minenwerkzeug",
"cost_silver": 3,
"cost_zynalith": 0,
"victory_points": 0,
"type": "equipment",
"description": "Kampf: Erhalte 1 Zynalith.",
"image": "mining_tools"
},
{
"name": "Lupe",
"cost_silver": 0,
"cost_zynalith": 0,
"victory_points": 0,
"type": "equipment",
"description": "Sofort: Erhalte 1 Zynalith.",
"image": "lupe"
},
{
"name": "Banner",
"cost_silver": 2,
"cost_zynalith": 0,
"victory_points": 0,
"type": "equipment",
"description": "Sofort: Sturmangriff.",
"image": "banner"
},
{
"name": "Rostige Klinge",
"cost_silver": 5,
"cost_zynalith": 0,
"victory_points": 1,
"type": "equipment",
"description": "Kampf: Gegnerwesen der Linie verlieren 1 HP.",
"image": "sword_1"
},
{
"name": "Krone",
"cost_silver": 3,
"cost_zynalith": 0,
"victory_points": 3,
"type": "equipment",
"description": "",
"image": "crown_1"
},
{
"name": "Brüchiger Talisman des Schutzes",
"cost_silver": 2,
"cost_zynalith": 0,
"victory_points": 0,
"type": "equipment",
"description": "Kampf: Falls dieses Wesen einen Kampf verlieren sollte, erhältst du in diesem Kampf keinen Schaden - zerstöre dann außerdem diese Ausrüstungs-Karte.",
"image": "talisman_1"
},
{
"name": "Schurken-Rucksack",
"cost_silver": 4,
"cost_zynalith": 0,
"victory_points": 0,
"type": "equipment",
"description": "Sofort: Lege eine Eigenschafts-Karte von einem gegnerischen Wesen unter ein eigenes.",
"image": "backpack"
},
{
"name": "Giftphiole",
"cost_silver": 3,
"cost_zynalith": 0,
"victory_points": 0,
"type": "equipment",
"description": "Sofort: Zerstöre ein Wesen mit ATK-Wert >= 7 (insgesamt).",
"image": "green_liquid_1"
},
{
"name": "Erste-Hilfe-Set",
"cost_silver": 5,
"cost_zynalith": 0,
"victory_points": 0,
"type": "equipment",
"description": "Kampf: Heile dieses Wesen voll.",
"image": "first_aid"
},
{
"name": "Poesie-Band",
"cost_silver": 12,
"cost_zynalith": 0,
"victory_points": 2,
"type": "equipment",
"description": "Spielende: Erhalte so viel Zynalith wie verbleibende HP auf diesem Wesen sind.",
"image": "green_book"
},
{
"name": "Kleine Landkarte",
"cost_silver": 3,
"cost_zynalith": 0,
"victory_points": 2,
"type": "equipment",
"description": "Passiv: Du kannst auch die Position deiner Wesen mit einem INIT-Unterschied von bis zu 1 vertauschen.",
"image": "map_small"
},
{
"name": "Große Landkarte",
"cost_silver": 6,
"cost_zynalith": 0,
"victory_points": 2,
"type": "equipment",
"description": "Passiv: Du kannst auch die Position deiner Wesen mit einem INIT-Unterschied von bis zu 2 vertauschen.",
"image": "map_big"
},
{
"name": "Gezinkter Würfel",
"cost_silver": 4,
"cost_zynalith": 0,
"victory_points": 0,
"type": "equipment",
"description": "Sofort: Vertausche von zwei Wesen die Magiekarten mit selben Kosten.",
"image": "die"
},
{
"name": "Diplomatie-Urkunde",
"cost_silver": 0,
"cost_zynalith": 0,
"victory_points": 1,
"type": "equipment",
"description": "Sofort: Gebe allen Mitspielern 3 Silber von dir, danach heilen sich alle Spieler voll.",
"image": "scroll_diplomatic"
},
{
"name": "Trauer-Kasse",
"cost_silver": 4,
"cost_zynalith": 0,
"victory_points": 1,
"type": "equipment",
"description": "Trauer: Erhalte 2 Silber.",
"image": "cashbox"
},
{
"name": "Gewürze",
"cost_silver": 3,
"cost_zynalith": 0,
"victory_points": 0,
"type": "equipment",
"description": "Trauer: Heile die HP von dir oder diesem Wesen um 2.",
"image": "spices"
},
{
"name": "Spurt-Sandalen",
"cost_silver": 1,
"cost_zynalith": 0,
"victory_points": 0,
"type": "equipment",
"description": "Passiv: Du kannst pro Zug 1 bis 2 Hauptaktionen durchführen.",
"image": "sandals"
},
{
"name": "Grab-Schaufel",
"cost_silver": 0,
"cost_zynalith": 0,
"victory_points": 0,
"type": "equipment",
"description": "Trauer: Ziehe eine Karte.",
"image": "shovel"
},
{
"name": "Leiser Dolch",
"cost_silver": 4,
"cost_zynalith": 0,
"victory_points": 0,
"type": "equipment",
"description": "Trauer: Erhalte 1 Zynalith.",
"image": "black_dagger"
},
{
"name": "Kriegserklärung",
"cost_silver": 5,
"cost_zynalith": 0,
"victory_points": 0,
"type": "equipment",
"description": "Passiv: Es gibt eine zusätzliche 6. Runde (außer bei einer Apokalypse).",
"image": "crow"
},
# neu
{
"name": "Wertpapier",
"cost_silver": 3,
"cost_zynalith": 0,
"victory_points": 0,
"type": "equipment",
"description": "Passiv: Dein nicht ausgegebenes Silber wird am Ende der Runde verdoppelt.",
"image": "wertpapier"
},
{
"name": "Blockade",
"cost_silver": 4,
"cost_zynalith": 0,
"victory_points": 0,
"type": "equipment",
"description": "Passiv: Du kannst durch Niederlagen auf den beiden Linien neben dieser keinen direkten Schaden erleiden.",
"image": "two_shields"
},
{
"name": "Piraten-Kanone",
"cost_silver": 4,
"cost_zynalith": 0,
"victory_points": 0,
"type": "equipment",
"description": "Passiv: Dieses Wesen verursacht Durchschlag-Schaden.",
"image": "canon"
},
{
"name": "Mael-Offiziers-Rüstung",
"cost_silver": 9,
"cost_zynalith": 0,
"victory_points": 2,
"type": "equipment",
"description": "Sofort: Sturmangriff. Passiv: Dieses Wesen verursacht Durchschlag-Schaden. Ausrüstung/Eigenschaft: Erhalte 1 Silber.",
"image": "armor2"
},
{
"name": "Sprengstoff",
"cost_silver": 5,
"cost_zynalith": 0,
"victory_points": 0,
"type": "equipment",
"description": "Tod: Falls von einem Wesen getötet, stirbt dieses.",
"image": "dynamite"
},
{
"name": "Silberpfeile",
"cost_silver": 2,
"cost_zynalith": 0,
"victory_points": 0,
"type": "equipment",
"description": "Kampf: Werfe bis zu 3 Silber ab und verursache so viel Schaden an einem Spieler.",
"image": "silver_arrows"
},
{
"name": "Glücksbringer-Ring",
"cost_silver": 7,
"cost_zynalith": 0,
"victory_points": 2,
"type": "equipment",
"description": "Passiv: Dein maximales Spielerleben erhöht sich um 10.",
"image": "ring"
},
{
"name": "Göttliches Relikt",
"cost_silver": 5,
"cost_zynalith": 0,
"victory_points": 2,
"type": "equipment",
"description": "Passiv: Du kannst beliebig viel Zynalith für je 3 Silber kaufen oder verkaufen.",
"image": "religion",
"changed": False,
},
{
"name": "Gut gestimmte Violine",
"cost_silver": 6,
"cost_zynalith": 0,
"victory_points": 1,
"type": "equipment",
"description": "Gier/Event/Zauber: Erhalte 4 Silber.",
"image": "violine",
"changed": True,
},
{
"name": "Dornen-Panzer",
"cost_silver": 4,
"cost_zynalith": 0,
"victory_points": 0,
"type": "equipment",
"description": "Sofort: Sturmangriff. Verteidigung: Verursache 1 Schaden.",
"image": "defense3",
"changed": True,
},
]

tmp = data
data = []
for i in tmp:
    if "changed" in i and i["changed"] == True:
        data.append(i)

with open("../card_data/equipment_and_spells", "w") as f:
    f.write(json.dumps(data))
