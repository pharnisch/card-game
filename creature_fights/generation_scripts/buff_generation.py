import json

data = [
{
"name": "Flink",
"cost_silver": 2,
"victory_points": 0,
"initiative": 2,
"attack": 0,
"defense": 1,
"health_points": 0,
"image": "fast_child"
},
{
"name": "Stark",
"cost_silver": 4,
"victory_points": 0,
"initiative": -1,
"attack": 2,
"defense": 0,
"health_points": 0,
"image": "strong_troll"
},
{
"name": "Wagemutig",
"cost_silver": 2,
"victory_points": 0,
"initiative": 1,
"attack": 1,
"defense": 0,
"health_points": 0,
"image": "elve_warrior"
},
{
"name": "Wohlgenährt",
"cost_silver": 4,
"victory_points": 0,
"initiative": 0,
"attack": 0,
"defense": -1,
"health_points": 6,
"image": "fat_king"
},
{
"name": "Arglistig",
"cost_silver": 5,
"victory_points": 0,
"initiative": -1,
"attack": 3,
"defense": -1,
"health_points": 0,
"image": "rogue"
},
{
"name": "Geduldig",
"cost_silver": 1,
"victory_points": 0,
"initiative": -5,
"attack": 0,
"defense": 0,
"health_points": 0,
"image": "quiet_orc"
},
{
"name": "Ungeduldig",
"cost_silver": 1,
"victory_points": 0,
"initiative": 5,
"attack": 0,
"defense": 0,
"health_points": 0,
"image": "goblin_auctioneer"
},
{
"name": "Ausgeglichen",
"cost_silver": 4,
"victory_points": 0,
"initiative": 0,
"attack": 1,
"defense": 1,
"health_points": 0,
"image": "quiet_human"
},
{
"name": "Steinern",
"cost_silver": 5,
"victory_points": 0,
"initiative": -1,
"attack": -1,
"defense": 3,
"health_points": 0,
"image": "stone_golem"
},
{
"name": "Verträumt",
"cost_silver": 1,
"victory_points": 0,
"initiative": -2,
"attack": -1,
"defense": -1,
"health_points": 4,
"image": "quiet_woman"
},
{
"name": "Siegessicher",
"cost_silver": 2,
"victory_points": 1,
"initiative": 0,
"attack": 0,
"defense": 0,
"health_points": 0,
"image": "strong_goblin"
},
{
"name": "Adelig",
"cost_silver": 4,
"victory_points": 2,
"initiative": 0,
"attack": 0,
"defense": 0,
"health_points": 0,
"image": "women_1"
},
{
"name": "Unverwundbar",
"cost_silver": 10,
"victory_points": 0,
"initiative": 0,
"attack": 0,
"defense": "x2",
"health_points": 0,
"image": "high_priestess"
},
{
"name": "Blutrünstig",
"cost_silver": 10,
"victory_points": 0,
"initiative": 0,
"attack": "x2",
"defense": 0,
"health_points": 0,
"image": "angry_dwarve"
},
]
tmp = data
data = []
for i in tmp:
    if "changed" in i and i["changed"] == True:
        data.append(i)

with open("../card_data/buffs", "w") as f:
    f.write(json.dumps(data))
