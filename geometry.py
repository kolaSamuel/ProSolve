"""
    After question type and shape have been identified
    Calls geometry to assign proper shape to solve problem.
"""

from collections import Counter
from utils import *


class Circle(object):

    def __init__(self, data):

        self.data = data
        self.loopTerminate = Counter()
        self.formulas = ['area = pi*radius**2',
                         'diameter = 2*radius',
                         'perimeter = 2*pi*radius',
                         ]

        # initialises formulas for SolutionGraph search
        self.solution = SolutionGraph(self.formulas)

    def __getitem__(self, query):
        """
        Finds query buy searching through Solution graph
        :param query:
        :return:
        """
        pass


shape_type = {"circle": Circle,
              }


def geometry(s_type, query):
    shape = shape_type[s_type]()
    return shape[query]
