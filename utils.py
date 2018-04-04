"""
Various tools and utilities used
"""
import sys
from collections import*


def insufficient_data_handler(query, data):

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
