from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


money_machine = MoneyMachine()
my_menu = Menu()
coffee_maker = CoffeeMaker()

# menu_item = MenuItem("Latte", 150, 50, 50, 1.5)
# print(menu_item.ingredients)
# coffee_maker.report()
# print(coffee_maker.is_resource_sufficient(menu_item))

coffee_machine_on = True
order = input("What would you like to drink?")
menu_item = Menu().find_drink(order)
# print(menu_item.ingredients)
# order = "latte"

while coffee_machine_on:
    options = my_menu.get_items()
    if order == "off":
        coffee_machine_on = False
    elif order == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        if my_menu.find_drink(menu_item.name).name == order and coffee_maker.is_resource_sufficient(menu_item):
            if money_machine.make_payment(menu_item.cost):
                coffee_maker.make_coffee(menu_item)

    order = input("What would you like to drink?")
    menu_item = Menu().find_drink(order)



