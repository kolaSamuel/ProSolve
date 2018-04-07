"""
Various tools and utilities used
"""
import sys
from sympy import solve, sympify, Eq, symbols


def equations(items, formulas):
    """
    Converts input string expression to function and stores
    :param items: string or list of string expressions
    :param formulas: list of functions
    :return:
    """
    error_messages = []

    if type(items) == str:
        items = [items]

    for i in range(len(items)):
        string = items[i]
        try:
            # right hand side and left hand sides of the equation
            lhs, rhs = string.split('=')
            formulas.append(Eq(symbols(lhs), sympify(rhs)))

        except ValueError as message:
            # Saves error(s) for display
            error_messages.append(str(message))


def insufficient_data_handler(query, data):

    """
    Checks if data is accurate ,tries again if not and terminates if accurate
    :param query: variable to be calculated given data
    :param data: available information to evaluate query
    :return: 0 that terminates or any other value ( which indicates a re-solve)
    """

    data_changes = 0

    print("Insufficient data given to compute, ", query)
    response = input("Confirm data? Y/N \n").strip()

    if response[:1].capitalize() == "Y":
        print("Input in format: variable <space> value",
              "Type 'done' when complete", sep='\n')
        for key in data:
            print(key, "-> ", data[key])
        print()
        try:
            variable, value = input("Input: ").strip().split()
            variable.lower()
        except ValueError:
            variable = 'done'

        while variable != 'done':
            data_changes += 1
            data[variable] = int(value)
            try:
                variable, value = input("Input: ").strip().split()
                variable.lower()
            except ValueError:
                variable = 'done'

        if data_changes:
            print("Attempting to Resolve problem...")

    return data_changes
