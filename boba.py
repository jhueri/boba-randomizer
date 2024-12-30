from random import choice

tea_bases = ["Green Tea", "Black Tea", "Oolong Tea"]
flavors = ["Wintermelon", "Caramel", "Mango"]
sugar_levels = ["0%", "50%", "100%"]
toppings = ["Boba Pearls", "Grass Jelly", "Pudding"]

def random_boba():
    return {
        "Tea Base": choice(tea_bases),
        "Flavor": choice(flavors),
        "Sugar Level": choice(sugar_levels),
        "Toppings": choice(toppings)
    }

print("Randomized Boba Drink:")
for key, value in random_boba().items():
    print(f"{key}: {value}")