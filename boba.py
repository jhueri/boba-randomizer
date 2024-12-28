from random import choice

boba = [["Green Tea", "Milk Foam Series", "Under 300 Calories"], ["Wintermelon", "Milk Foam Series", "Under 500 Calories"],
        ["Caramel Milk Tea", "Milk Tea Series", "Under 500 Calories"]]

print("Select from the Milk Foam Series or the Milk Tea Series?")
series = input()

for item in boba:
    if item[1] == series:
        print (series + " boba: " + item[0])