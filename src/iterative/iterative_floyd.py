"""
Floyd's Algorithm Implementation

This module implements a simple version of Floyd's algorithm for computing the
shortest paths in a graph. It contains these main functions:
- main: Controls the execution of the script.
- print_out_graph: Outputs the graph with node distances.
- iterative_floyd: Computes the shortest path.

Global variables:
- NO_PATH: Marker for no paths (set to sys.maxsize).
- GRAPH: Adjacency matrix containing distances between nodes.
- MAX_LENGTH: Graph dimension.
- NO_PATH_MARKER: Placeholder for unreachable paths in the output.
"""

from itertools import product
from sys import maxsize
NO_PATH: int = maxsize
GRAPH: list[list[int]] = [
    [0, 7, NO_PATH, 8],
    [NO_PATH, 0, 5, NO_PATH],
    [NO_PATH, NO_PATH, 0, 2],
    [NO_PATH, NO_PATH, NO_PATH, 0],
]
MAX_LENGTH: int = len(GRAPH[0])
NO_PATH_MARKER: str = "No Path"


def main() -> None:
    """
    Execute Floyd's Algorithm using an iterative approach and display the results.
    """
    iterative_floyd()
    print_out_graph()


def print_out_graph() -> None:
    """
    This function prints out the graph with the distances
    and a placeholder for no path between nodes
    """
    for start_node in range(0,MAX_LENGTH):
        for end_node in range(0,MAX_LENGTH):
            distance = GRAPH[start_node][end_node]
            if distance == NO_PATH:
                distance = NO_PATH_MARKER

            print(f"Distance from Node {start_node} to Node {end_node} is {distance}")


def iterative_floyd() -> None:
    """
    Compute the shortest paths for all pairs of nodes using Floyd's algorithm.
    """
    for intermediate, start_node, end_node in product(
    range(MAX_LENGTH),range(MAX_LENGTH), range(MAX_LENGTH)):

           if start_node == end_node:
               GRAPH[start_node][end_node] = 0
               continue
           
           GRAPH[start_node][end_node] = min(GRAPH[start_node][end_node],
            GRAPH[start_node][intermediate] + GRAPH[intermediate][end_node] )
if __name__ == "__main__":
    main()
