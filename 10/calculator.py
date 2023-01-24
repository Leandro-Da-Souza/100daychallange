import operator
import os
from art import logo


def clear():
    # for windows
    if os.name == 'nt':
        _ = os.system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = os.system('clear')



def calculator(operation, a, b):
    """Simple calculator function with add, subtract, multiply, divide operations."""

    operations = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv
    }

    if isinstance(operation, str) == False or operation not in operations:
        return 'Please provide a valid operator.'
    return f"{a} {operation} {b} = {operations[operation](a,b)}"


def run_calc():
    is_running = True
    print(logo)
    a = int(input('First number: '))

    while is_running:
        b = int(input('Next number: '))
        print('Please choose between these operations: + - * /')
        ops = input('Operation: ')
        print(calculator(ops, a, b))

        if input('Continue? Y or N: ') == 'y':
            a = b
        else:
            is_running = False
            run_calc()

run_calc()