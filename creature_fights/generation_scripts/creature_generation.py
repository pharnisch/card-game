
import random
import json

AMOUNT = 50
MIN_COST = 0
MAX_COST = 20
ITEM_POINTS_SCALE = 2

class Creature:
    def __init__(self):
        self.data = {
            "name": "Platzhalter des Ogertums",
            "initiative": random.randrange(0, 10+1),  # mid from 0 to 10
            "attack": 0,
            "defense": 0,
            "health_points": 1,
            "cost_silver": 0,
            "victory_points": 0,
            "equipment_slot": False,
            "spell_slot": False,
        }

        self.set_random_name()

        self.data["cost_silver"] = random.randrange(MIN_COST, MAX_COST+1)

        self.item_points = self.data["cost_silver"] * ITEM_POINTS_SCALE

        if self.data["cost_silver"] >= 3:
            per_cent = random.randrange(0, 100)
            if per_cent < 10:
                self.data["equipment_slot"] = True
                self.data["spell_slot"] = True
                self.item_points -= 3 * ITEM_POINTS_SCALE
                print(f"bought both slots for 3 silver")
            elif per_cent < 40:
                self.data["spell_slot"] = True
                self.item_points -= 2 * ITEM_POINTS_SCALE
                print(f"bought one slot for 2 silver")
            elif per_cent < 70:
                self.data["equipment_slot"] = True
                print(f"bought one slot for 2 silver")

        while self.item_points > 0:
            self.spend_random_points()

    def spend_random_points(self):
        per_cent = random.randrange(0, 100)
        if per_cent < 10:
            if self.item_points >= 2 * ITEM_POINTS_SCALE:
                self.data["victory_points"] += 1
                self.item_points -= 2 * ITEM_POINTS_SCALE
                print(f"bought one VP for 2 silver")
        elif per_cent < 30:
            if self.item_points >= 1 * ITEM_POINTS_SCALE:
                self.data["health_points"] += 1
                self.item_points -= 1 * ITEM_POINTS_SCALE
                print(f"bought one HP for 1 silver")
        elif per_cent < 65:
            current_cost = 0.5
            if self.data["defense"] > 3:
                current_cost = 1
            if self.data["defense"] > 5:
                current_cost = 2
            if self.data["defense"] > 7:
                current_cost = 4
            if self.item_points >= current_cost * ITEM_POINTS_SCALE:
                self.data["defense"] += 1
                self.item_points -= current_cost * ITEM_POINTS_SCALE
                print(f"bought one DEF for {current_cost} silver")
        elif per_cent < 100:
            current_cost = 0.5
            if self.data["attack"] > 3:
                current_cost = 1
            if self.data["attack"] > 5:
                current_cost = 2
            if self.data["attack"] > 7:
                current_cost = 4
            if self.item_points >= current_cost * ITEM_POINTS_SCALE:
                self.data["attack"] += 1
                self.item_points -= current_cost * ITEM_POINTS_SCALE
                print(f"bought one ATK for {current_cost} silver")

    def set_random_name(self):
        volk = ["Oger", "Elfen", "Zwerge", "Menschen", "Goblins", "Gar'daa", "Lichtwesen", "Dämonen"]
        beruf = ["Schmied", "Kürchner", "Bastler", "Künstler", "Techniker", "Alchemist", "Händler", "Schurke", "Gefährte", "Reisender", "Diplomat", "Krieger"]
        adjektive = [ "Abgesandter", "Gesegneter", "Einfacher", "Tollkühner", "Verlachter", "Heimtückischer", "Lustiger", "Trauriger", "Einsamer"]
        name = "" + adjektive[random.randrange(0,len(adjektive))] + " " + beruf[random.randrange(0,len(beruf))] + " der " + volk[random.randrange(0,len(volk))]
        self.data["name"] = name

    def __str__(self):
        return json.dumps(self.data)




creatures = [Creature().data for i in range(AMOUNT)]
with open("../card_data/creatures", "w") as f:
    f.write(json.dumps(creatures))
