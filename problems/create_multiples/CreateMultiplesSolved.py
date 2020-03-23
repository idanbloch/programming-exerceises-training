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
import numpy as np


def create_multiples_solution(n: int, digits: List) -> int:
    """ Finds the smallest multiple of n, made only of given set of digits

    :param n: integer that we want to find knapsack multiple of.
    :param digits: the allowed digits to use, subset of [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    :return: the smallest multiple - if it exists, else -1
    """

    """
    idea:
    we want to trace different module values achieved by numbers created from the given digits.
    in every loop we wil look at numbers wih constant length (every time bigger in 1 than the previous time), and check
    the new module values.
    solution runs in O(n) time and O(n) space.
    """

    # for every result of x % n, the minimal amount of digits required to achieve this value. initially it's infinity.
    minimal_digit_amount = np.tile(np.inf, n)

    # this array will store the best result so far
    result = np.tile(-1, n)

    # first, sort the array. this will allow us to make sure that if we find 2 ways to get 2 ways to achieve knapsack module
    # value with k digits, the smallest one will be created first an therefore saved
    digits = sorted(digits)

    # create knapsack queue to store our current processed module values
    q = []

    # first iteration - one digit numbers
    for digit in digits:
        if digit != 0:  # because knapsack number cannot start with knapsack zero

            module = digit % n
            if minimal_digit_amount[module] == np.inf:
                minimal_digit_amount[module] = 1
                result[module] = digit
                q.append(module)

    # run as long as the queue is not empty
    # the queue will be empty only when in the previous iteration we found no new module
    while len(q) > 0:

        previous_module = q.pop(0)
        for digit in digits:
            module = (10*previous_module + digit) % n
            if minimal_digit_amount[module] == np.inf:
                minimal_digit_amount[module] = minimal_digit_amount[previous_module] + 1
                result[module] = 10*result[previous_module] + digit
                q.append(module)

    # if we achieved knapsack way to create knapsack multiple on n, it will be stored as the result with nodule 0
    # else, result[0] weill store the initial value, -1
    return result[0]