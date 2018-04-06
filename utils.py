"""
Various tools and utilities used
"""
import sys
from collections import Counter
from sympy import solve, sympify, Eq, symbols


def equation(items):
    equation_errors = []

    if type(items) == str:
        items = [items]

    for i in range(len(items)):
        string = items[i]
        try:
            # right hand side and left hand sides of the equation
            rhs, lhs = string.split('=')
        except ValueError as message:
            equation_errors.

def insufficient_data_handler(query, data):

    """
    Checks if data is accurate ,tries again if not and terminates if accurate
    :param query: variable to be calculated given data
    :param data: available information to evaluate query
    :return: 0 that terminates or any other value ( which indicates a re-solve)
    """

    data_changes = 0

    print("Insufficient data given to compute, ", query)
    response = input("Confirm data? Y/N").strip()

    if response[:1].capitalize() == "Y":
        print("Input in format variable value",
              "Type 'done' when complete", sep='\n')
        for key in data:
            print(key, "-> ", data[key])
        print()
        variable, value = input("Input: ").strip().split()

        while variable != 'done':
            data_changes += 1
            data[variable] = int(value)

        if data_changes:
            print("Attempting to Resolve problem...")

    return data_changes
