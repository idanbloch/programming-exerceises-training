"""
problem formalization:

you are given an unweighted (directed or undirected) graph with N nodes, numbered from 0 to N-1. In addition you are given number
between 0 to N-1 representing one of the nodes (source). Compute, for every node in the graph, the amount of different
paths from the source to the node that are shortest.

Create an EFFICIENT algorithm to perform the given task.

-----------------------------------------------------------------------------------------------------------------------

Example:

input: shown in graph.jpg, source: 1
output: [1, 1, 1, 2, 2, 2, 4]

(the paths to node 6:
0 -> 1 -> 3 -> 4 -> 6
0 -> 1 -> 3 -> 5 -> 6
0 -> 2 -> 3 -> 4 -> 6
0 -> 2 -> 3 -> 5 -> 6)

(the process of rotation/root changing is shown in rotated_tree.jpg)

-----------------------------------------------------------------------------------------------------------------------

Limitations:

time - 5 seconds
space - no limitation

-----------------------------------------------------------------------------------------------------------------------

Testing:

After implementing your solution, test it with out given input by 'CheckSolution' file.
You have a total of 10 test:
- tests 1-5 are visible to you, and you can access it's input using 'get_input' method from utils.Test.
- tests 6-10 are not visible to you, and need to pass them without knowing the input.
It is assured to you that all input is legal and fits the solution signature.

-----------------------------------------------------------------------------------------------------------------------

Documentation:

After passing all tests, write a doc in Confluence describing your solution.
In the doc, analyze the runtime of the algorithm you used.

"""

from typing import List
import networkx as nx


def shortest_path_amount_solution(path_to_graph: str, source: int) -> List[int]:
    """ Finds for each node the amount of different possible paths from source to it that have the shortest path

    :param path_to_graph: path to the pickle file with the graph input
    :param source: the number od the wanted source
    :return: array with the amount of shortest paths
    """
    g = nx.read_gpickle(path_to_graph)
    pass
