import menu as m
import resouces


def menu_status(item_menu):
    if m.MENU[item]['available']:
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


switch_on = True

while switch_on:
    # show options to user and cost to select
    print("Wellcome to WellExpress.")
    print("Choose an option:")

    for item in m.MENU.keys():
        print(f"{m.MENU[item]['id']}.{item.upper()}: Cost $: {m.MENU[item]['cost']} ({menu_status(m.MENU[item])}).")

    choice = int(input("What do you wish? Type the code: "))

    # report that bring the balance of resources
    if choice == 99:
        print("====== Report of resources available: ======")
        for resource in resouces.resources:
            print(f"{resource.upper()} : {resouces.resources[resource]}")
        # TODO: insert breakdown here

    # process of collect the coins
    coins_inserted = {
        "quarter": [],
        "dimes": [],
        "nickel": [],
        "pennies": []
    }
    print("Please, insert the coins:")

    for c in coins_inserted.keys():
        coins_inserted[c] = int(input(f"How many {c}? "))

    print(f"Amount of coins inserted: $ {coins_amount()}")

# TODO: create a function to check if the resources are enough to make the dring

# TODO: add clear on loop

# TODO: turn off the machine when code 'off'

# TODO: create a function do deduce or increase resources

# TODO: create a function to check if the coins are enough and give the change

# TODO: create a money balance that is update by transaction proceeded

# TODO: after a process, check if menu still available to select
