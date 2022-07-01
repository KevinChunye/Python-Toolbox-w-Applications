MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
print(MENU["cappuccino"]["cost"])

profit = 0
is_on = True

def is_resource_efficient(order_ingredients):
    is_enough = True
    for item in order_ingredients:
        """returns true when order can be made, false is the order is lack of enough ingredients"""
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}")
            is_enough= False
            return is_enough
    return is_enough

def process_coins():
    """returns the total calculated from coins inserted"""
    print("Please insert coins")
    total = int(input("How many quarters?: ")) *0.25
    total += int(input("How many dimes?: ")) * 0.1
    total += int(input("How many nickles?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total

def make_coffee(drink_name, order_ingredients):
    """deduct the required ingredients from the resources"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"here is your {drink_name}")

def is_transaction_successful(money_received, drink_cost):
    """return true when the payment is accepted or false if money is not enough"""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost,2)
        print(f"here is ${change} change")
        global profit
        profit += drink_cost
        return True
    else:
        print("sorry that's not enough money. Money refunded")
        return False
while is_on:
    choice = input("What would you like espresso/latte/cappuccino: (type the name you want)")
    if choice =="off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']} ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if is_resource_efficient(drink['ingredients']):
            payment = process_coins()
            if is_transaction_successful(payment,drink['cost']):
                make_coffee(choice,drink['ingredients'])
