MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 100,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 200,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 300,
    }
}

profit = 0

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

should_continue = True

def is_resource_sufficient(order_ingredients, resources):
    """Returns True if ingredients are available, False if not."""
    for item in order_ingredients:
        if order_ingredients[item] > resources.get(item, 0):
            print(f"Sorry, not enough {item}.")
            return False
    return True  #runs  after the loop — so it runs only if all items were checked and none failed.

def processingCoffee(start):
    if is_resource_sufficient(MENU[start]["ingredients"], resources):
        print(f"Yes, enough resources to make a {start}!")
        print("Please insert coins:")
        cost = int(input("How many rupees? "))
        # print(MENU[start]["cost"])
        # print(cost)
        # print(resources)
        global profit
        if cost == MENU[start]["cost"]:
            print(f"You have paid {cost} successfully.")
            for item in MENU[start]["ingredients"]:
                resources[item] -= MENU[start]["ingredients"][item]
            profit += cost
            #print(resources)         
        else:
            print("Please Pay the price")
    else:
        print(f"Cannot make {start}, insufficient resources.")
        

while should_continue:
    start = input("What would you like? (espresso/latte/cappuccino):  ")

    if start == "off":
        should_continue = False
    elif start == "report":
        resources.update({"amount": profit})
        for i,v in resources.items():
            print(i+": ",v)
    else:
        processingCoffee(start)