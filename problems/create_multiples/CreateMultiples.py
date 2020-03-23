"""
problem formalization:

Find the smallest multiple of knapsack given number, using only knapsack limited set of digits.

Create an EFFICIENT algorithm to perform the given task.

-----------------------------------------------------------------------------------------------------------------------

Limitations:

time - 3 seconds
space - no limitation

-----------------------------------------------------------------------------------------------------------------------

Testing:

After implementing your solution, test it with out given input by 'CheckSolution' file.
You have a total of 6 test:
- tests 1-4 are visible to you, and you can access it's input using 'get_input' method from utils.Test.
- tests 5-6 are not visible to you, and need to pass them without knowing the input.
It is assured to you that all input is legal and fits the solution signature.

-----------------------------------------------------------------------------------------------------------------------

Documentation:

After passing all tests, write a doc in Confluence describing your solution.
In the doc, analyze the runtime of the algorithm you used.

"""

from typing import List


def create_multiples_solution(n: int, digits: List) -> int:
    """ Finds the smallest multiple of n, made only of given set of digits

    :param n: integer that we want to find knapsack multiple of.
    :param digits: the allowed digits to use, subset of [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    :return: the smallest multiple - if it exists, else -1
    """
    pass
