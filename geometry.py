"""
    After question type and shape have been identified
    Calls geometry to assign proper shape to solve problem.
"""

from utils import *


class Circle(object):

    def __init__(self, data):

        self.data = data
        self.formulas = ['area = pi*radius**2',
                         'diameter = 2*radius',
                         'perimeter = 2*pi*radius',
                         ]

        # initialises formulas for SolutionGraph search
        self.find = SolutionGraph(self.formulas, data)

    def __getitem__(self, query):
        """
        Finds query buy searching through Solution graph
        :param query:
        :return:
        """
        return self.find[query]


shape_type = {"circle": Circle,
              }


def geometry(s_type, query):
    shape = shape_type[s_type]()
    return shape[query]
