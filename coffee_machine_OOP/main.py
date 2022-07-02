from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

is_on = True

# misson 1 print report
money_machine.report()
coffee_maker.report()

while is_on:
    options = menu.get_items()
    choice = input(f"what would you like? ({options})")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()
    else:
        drink = menu.find_drink(choice)
        print(money_machine.make_payment(drink.cost))



