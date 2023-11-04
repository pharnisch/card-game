import json

data = [
{
"name": "Flink",
"cost_silver": 2,
"victory_points": 0,
"initiative": 2,
"attack": 0,
"defense": 1,
"health_points": 0
},
{
"name": "Stark",
"cost_silver": 4,
"victory_points": 0,
"initiative": -1,
"attack": 2,
"defense": 0,
"health_points": 0
},
{
"name": "Wagemutig",
"cost_silver": 2,
"victory_points": 0,
"initiative": 1,
"attack": 1,
"defense": 0,
"health_points": 0
},
{
"name": "Wohlgenährt",
"cost_silver": 4,
"victory_points": 0,
"initiative": 0,
"attack": 0,
"defense": -1,
"health_points": 6
},
{
"name": "Arglistig",
"cost_silver": 5,
"victory_points": 0,
"initiative": -1,
"attack": 3,
"defense": -1,
"health_points": 0
},
{
"name": "Geduldig",
"cost_silver": 1,
"victory_points": 0,
"initiative": -5,
"attack": 0,
"defense": 0,
"health_points": 0
},
{
"name": "Ungeduldig",
"cost_silver": 1,
"victory_points": 0,
"initiative": 5,
"attack": 0,
"defense": 0,
"health_points": 0
},
{
"name": "Ausgeglichen",
"cost_silver": 4,
"victory_points": 0,
"initiative": 0,
"attack": 1,
"defense": 1,
"health_points": 0
},
{
"name": "Steinern",
"cost_silver": 5,
"victory_points": 0,
"initiative": -1,
"attack": -1,
"defense": 3,
"health_points": 0
},
{
"name": "Verträumt",
"cost_silver": 1,
"victory_points": 0,
"initiative": -2,
"attack": -1,
"defense": -1,
"health_points": 4
},
{
"name": "Siegessicher",
"cost_silver": 2,
"victory_points": 1,
"initiative": 0,
"attack": 0,
"defense": 0,
"health_points": 0
},
{
"name": "Adelig",
"cost_silver": 4,
"victory_points": 2,
"initiative": 0,
"attack": 0,
"defense": 0,
"health_points": 0
},
{
"name": "Unverwundbar",
"cost_silver": 10,
"victory_points": 0,
"initiative": 0,
"attack": 0,
"defense": "x2",
"health_points": 0
},
{
"name": "Blutrünstig",
"cost_silver": 10,
"victory_points": 0,
"initiative": 0,
"attack": "x2",
"defense": 0,
"health_points": 0
},
]

with open("../card_data/buffs", "w") as f:
    f.write(json.dumps(data))
