"""
Various tools and utilities used
"""
from sympy import solve, sympify, Eq, symbols
from collections import defaultdict, OrderedDict
from datascience import Table


class Node(Table):
    """
        pre- initialized table class
        Note to future self:
            You might be experiencing some indexing or table related errors
            it's not you it's me. Don't worry i gatchu just change the Node
            to a  default object type then create a table within it. Don't
            forget to create all table methods you used too. Lol, I'm sorry,
            I actually thought it would make life easier. So..., How are you?
    """
    def __init__(self):
        Table.__init__(self)
        self._columns = OrderedDict(
            {'Equation': [],
             'Symbols': [],
             'Complexity': [],
             }
        )


class SolutionGraph(object):
    """
        A cyclic graph that connects all inter-related equations to themselves
        to convert problem into search problem.
    """

    def __init__(self, equations):
        self.tree = defaultdict(Node)

        # build/Initialize graph
        for equation in equations:
            self.add_equation(equation)
        for node in self.tree:
            self.tree[node].sort('Complexity')

    def add_equation(self, equation):
        """
        Converts input string expression to function and stores
        :param equation:
        :return:
        """
        try:
            lhs, rhs = equation.split('=')
            formula = Eq(symbols(lhs), sympify(rhs))
            variables = formula.free_symbols
            for variable in variables:
                new_formula = Eq(variable, solve(formula, variable)[-1])
                row = [new_formula, variables.difference([variable]), len(variables)-1]
                # print('\n before', self.tree[variable].table, sep='\n')
                self.tree[variable] = self.tree[variable].with_row(row)
                # print('\n after', self.tree[variable].table, sep='\n')

        except ValueError:
            print('Equation Error: Invalid expression ',
                  equation, '\n \t Ignoring expression...\n')
            pass

    def __str__(self):
        string = ''
        for node in self.tree:
            string += "\n" + str(node) + " :\n" + self.tree[node].__str__() + '\n'
        return string


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
