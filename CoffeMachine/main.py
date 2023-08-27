from data import MENU, resources, profit

# print(MENU, resources, profit)

QUARTER = 0.25
DIME = 0.10
NICKLE = 0.05
PENNY = 0.01

def user_order():
    """decide what to make next."""
    return input("What would you like? (espresso/latte/cappuccino/report): ")

def check_resource(order):
    """check if there is enough resource for making a coffee."""
    for i in MENU[order]["ingredients"]:
        if MENU[order]["ingredients"][i] > resources[i]:
            print(f"Sorry,there is not enough {i}.")
            return False
    return True

def check_transaction(order):
    """Check if the money insert is enough to pay the order."""
    print("Please insert coins.")
    quarter_count = int(input("How many quarters? "))
    dime_count = int(input("How many dimes? "))
    nickle_count = int(input("How many nickles? "))
    penny_count = int(input("How many pennies? "))
    money_insert = QUARTER * quarter_count + DIME * dime_count + NICKLE * nickle_count + PENNY * penny_count
    change = round((money_insert - MENU[order]["cost"]), 2)
    if change > 0:
        print(f"Here is ${change} in change.")
        return True
    elif change == 0:
        return True
    else:
        print("There is not enough money.Money refund.")
        return False

def make_coffee(order):
    """Make a coffee by deducte the ingredients of the order."""
    for i in MENU[order]["ingredients"]:
        resources[i] -= MENU[order]["ingredients"][i]
    print(f"Here is your {order}.Enjoy!")


is_on = True
transaction_complate = True
while is_on:
    order = user_order()
    if order == "report":
        print(resources, profit)
    elif order == "off":
        is_on = False
    elif order in MENU:
        if check_resource(order):
            # reduce the ingredients
            transaction_complate = check_transaction(order)
            if transaction_complate:
                profit += MENU[order]["cost"]
                make_coffee(order)            
            else:
                print("Please order again.")
        else:
            is_on = False
    else:
        print("Please input the right direction.")
