from utils import equations
from collections import Counter
from timeit import timeit

A = []


def tester():
    equations(['area = pi*radius**2',
               'diameter = 2*radius',
               'perimeter = 2*pi*r',
               ], A)


print('functions: ', timeit("tester()", setup="from __main__ import tester, A", number=10))
print('ranges: ', timeit("range(10**6)", setup="from __main__ import tester, A", number=10))

