"""
problem formalization:

you are given an unweighted directed graph with N nodes, numbered from 0 to N-1. In addition you are given number
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
import numpy as np
import os


def shortest_path_amount_solution(path_to_graph: str, source: int) -> List[int]:
    """ Finds for each node the amount of different possible paths from source to it that have the shortest path

    :param path_to_graph: path to the pickle file with the graph input
    :param source: the number od the wanted source
    :return: array with the amount of shortest paths
    """

    """
    idea:
    we iterate the graph from source by BFS. when we find a new shortest path to node, to set its path amount to be the
    same ad the node we arrived from, and when we find a new path with same distance as the current shortest path we
    update the counter by the amount of paths to node we arrived from.
    """

    g = nx.read_gpickle(os.path.join(os.getcwd(), path_to_graph))
    n = len(g.nodes)

    dists = np.tile(np.inf, n)  # length of shortest path to each node so far
    dists[source] = 0
    amount = np.zeros(n)  # amount of paths found with the same length as the current shortest path
    amount[source] = 1

    # Pay attention that we used edge_bfs and not bfs_edges. that's because bfs_edges will remember the visited nodes
    # and will not contains another edges towards them - and using it will give us a perfect dists array but amount
    # array will be the same as np.ones(n). But edge_bfs iterate over *all* edges in a bfs order, thus helps us.
    for u, v in nx.edge_bfs(g, source):
        if dists[u] + 1 < dists[v]:
            dists[v] = dists[u] + 1
            amount[v] = amount[u]
        elif dists[u] + 1 == dists[v]:
            amount[v] += amount[u]

    return list(amount)
