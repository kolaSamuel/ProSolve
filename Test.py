from utils import SolutionGraph
from collections import Counter
from timeit import timeit
from geometry import *
import numpy as np

A1 = np.array(range(200))
A = list(range(200))

B = ['area = pi*radius**2', 'diameter = 2*radius', 'perimeter = 2*pi*radius', 'thy = trt = 3']
data = {"radius": 3}
find = {"area"}
question = Circle(data, find)
print(question["area"])
print(question["radius"])
print(question["theta"])


