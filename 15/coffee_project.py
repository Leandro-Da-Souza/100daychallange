"""
Makes 3 different flavours
Each flavour has
1. A price
2. Water Quantity
3. Coffee Quantity
Depending on the flavour there is option to add quantity of Milk.

Is coin operated, will take
A penny = 1 cent = 0.01
A dime = 10 cents = 0.10
A nickel = 5 cents = 0.05
A Quarter = 25 cents = 0.25

1. Print report, tell how much of the resources it has left
2. Check if resources are sufficient
3. Process coins
4. Check if transaction is successful
5. If above 3 successful, make coffee
"""

from resources import MENU, resources

coins_dictionary = {
    'quarter': 0.25,
    'dime': 0.10,
    'nickel': 0.05,
    'penny': 0.01
}

bank = 0


def print_resources():
    """
    Print the resources and quantity (milk, water, coffee)
    :return:
    """
    for n in resources:
        if n == 'coffee':
            print(f"{n}: {resources[n]} g")
        else:
            print(f"{n}: {resources[n]} ml")


def make_order():
    return input('What would you like to order? choose between espresso/cappuccino/latte: ')


def check_resources(order: str):
    """
    check if the resources in the order are available, return dict of True / False for each resource
    :param order:
    :return:
    """
    ingredients = MENU[order]['ingredients']
    check_list = {}

    for n in ingredients:
        if resources[n] > ingredients[n]:
            check_list[n] = True
        else:
            check_list[n] = False

    return check_list


def calculate_cost(coin, times):
    return coin * times


def coffee_machine():
    is_running = True

    while is_running:
        
        order = make_order()

        if order.lower() == 'report':
            print_resources()
            coffee_machine()
        elif order.lower() == 'off':
            print('Turning off.')
            break
        else:
            while True:
                if order in MENU:
                    break
                else:
                    print('Sorry, i did not understand you.')
                    order = make_order()

        check_order = check_resources(order)
        for key, val in check_order.items():
            if not val:
                print(f"Sorry, not enough {key} to make order.")
                print('Turning off.')
                return
            else:
                resources[key] -= MENU[order]['ingredients'][key]

        cost = MENU[order]['cost']
        print(f"Please insert {cost}.")
        payment = 0

        for coin in coins_dictionary:
            coin_input = int(input(f"How many {coin}s would you like to insert? "))
            payment += calculate_cost(coins_dictionary[coin], coin_input)

        while cost > payment:
            print(f"Not enough balance, please insert {(cost - payment):.2f} more.")
            for coin in coins_dictionary:
                coin_input = int(input(f"How many {coin}s would you like to insert? "))
                payment += calculate_cost(coins_dictionary[coin], coin_input)

        if payment > cost:
            change = payment - cost
            print(f"Your change is {change:.2f}.")

        print(f'Please enjoy your {order}.')


coffee_machine()
