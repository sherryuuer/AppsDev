from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
# drink = MenuItem()
menu = Menu()

is_on = True
transaction_complate = True
while is_on:
    order = input("What would you like? (espresso/latte/cappuccino/report): ")
    if order == "report":
        coffee_maker.report()
        money_machine.report()
    elif order == "off":
        is_on = False
    elif order in menu.get_items():
        drink = menu.find_drink(order)
        if coffee_maker.is_resource_sufficient(drink):
            transaction_complate = money_machine.make_payment(drink.cost)
            if transaction_complate:
                coffee_maker.make_coffee(drink)
            else:
                print("Please order again.")
        else:
            is_on = False
    else:
        print("Please input the right direction.")
