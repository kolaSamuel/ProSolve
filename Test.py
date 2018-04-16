from utils import SolutionGraph
from collections import Counter
from timeit import timeit
import numpy as np

A1 = np.array(range(200))
A = list(range(200))

B = ['area = pi*radius**2', 'diameter = 2*radius', 'perimeter = 2*pi*radius', 'thy = trt = 3']
tree = SolutionGraph(B)
print(tree)

# def tester():
#     equations(['area = pi*radius**2',
#                'diameter = 2*radius',
#                'perimeter = 2*pi*r',
#                ], A)
#
#
# print('functions: ', timeit("1*2", setup="from __main__ import tester, A, A1"))
# print('ranges: ', timeit("A1*2", setup="from __main__ import tester, A, A1"))

