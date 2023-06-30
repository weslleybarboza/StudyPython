import menu as m
import resouces
from replit import clear


def menu_status(item_menu):
    if menu_available[item]['available']:
        return "Available"
    else:
        return "Unavailable"


def coins_amount():
    """Return total of value inserted"""
    amount = 0
    idx = 0
    for type_coin in coins_inserted.keys():
        if type_coin == "quarter":
            idx = 0.25
        elif type_coin == "dimes":
            idx = 0.10
        elif type_coin == "nickel":
            idx = 0.05
        else:
            idx = 0.01
        amount += coins_inserted[type_coin] * idx
    return round(amount, 2)


def check_money_enough(choice_item, total_coins):
    if choice_item["cost"] <= total_coins:
        return True
    else:
        return False


def update_resource(choice_item):
    """Decrease the resource available for the next drinks."""
    for ingredient in choice_item["ingredients"]:
        resouces_available[ingredient] -= choice_item["ingredients"][ingredient]
    return


def update_menu_status():
    """Check if item of menu has resource enough to sell the drink."""
    for product in menu_available.keys():
        for item in menu_available[product]["ingredients"]:
            if resouces_available[item] < menu_available[product]["ingredients"][item]:
                menu_available[product]["available"] = False


def check_change(amount_paid, choise):
    if choise["cost"] < amount_paid:
        print(f"Please, get your $ {amount_paid - choise['cost']} in change.")


def update_sell_balance(product_name):
    if product_name in sell_balance:
        sell_balance[product_name] += 1
    else:
        sell_balance[product_name] = 1


# setting init
switch_on = True
profit = 0
sell_balance = {}

# loading parameters
resouces_available = resouces.resources
menu_available = m.MENU

while switch_on:
    clear()

    # show options to user and cost to select
    print("Wellcome to WellExpress.")
    print("These are the option:")

    for item in menu_available.keys():
        if menu_available[item]["available"]:
            print(
                f"{menu_available[item]['id']}.{item.upper()}: Cost $: {menu_available[item]['cost']} ({menu_status(menu_available[item])}).")

    # process of collect the coins
    coins_inserted = {
        "quarter": [],
        "dimes": [],
        "nickel": [],
        "pennies": []
    }

    sell_process = True
    while sell_process:

        # process of choice and process an option
        choice_id = int(input("What do you wish? Type the code: "))

        choice_item = ''
        choice_product_name = ''
        for menu_item in menu_available:
            if menu_available[menu_item]["id"] == choice_id:
                choice_item = menu_available[menu_item]
                choice_product_name = menu_item

        # report that bring the balance of resources
        if choice_id == 99:
            print("====== Report of resources available: ======")
            for resource in resouces.resources:
                print(f"{resource.upper()} : {resouces.resources[resource]}")
            print(f"We have: $ {profit} in your pocket")
            print("====== Report end ======")
            sell_process = False
        elif choice_id == 100:
            print("Switching off the Machine...")
            sell_process = False
            switch_on = False
        else:
            print("Please, insert the coins:")
            for c in coins_inserted.keys():
                coins_inserted[c] = int(input(f"How many {c}? "))

            print(f"Amount of coins inserted: $ {coins_amount()}")

            if check_money_enough(choice_item, coins_amount()):
                profit += coins_amount()
                print("I'm preparing your drink =).")
                update_resource(choice_item)
                update_menu_status()
                check_change(coins_amount(), choice_item)
                update_sell_balance(choice_product_name)
                print("Get you drink!! Thank you")
                sell_process = False
            else:
                print("The amount of coins is NOT enough. Please insert more.")