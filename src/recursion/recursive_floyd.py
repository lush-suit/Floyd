"""
This module has a simple implementation of Floyd's Algorithm
It contains three main functions:
    main -> controls the execution of the script
    print_out_graph -> prints out the graph with nodes and distances
    recursive_floyd_warshall -> computes shortest path

The global variables are:
    NO_PATH = Marker for where there is no path. This is the max value of an integer
    GRAPH = Contains the distances for the graph. Node names are inferred by the position
    of the node, i.e. position  0 0 in the list is node 0
    MAX_LENGTH = The size of the graph
    MIN_LEVEL = The lowest search level for the shortest path calculation
    NO_PATH_MARKER = Holder for no path possible. This is used for the printing function. 
"""
from sys import maxsize
NO_PATH: int = maxsize
GRAPH: list[list[int]] = [[0, 7, NO_PATH, 8],
[NO_PATH, 0, 5, NO_PATH],
[NO_PATH, NO_PATH, 0, 2],
[NO_PATH, NO_PATH, NO_PATH, 0]]
MAX_LENGTH = len(GRAPH[0])
MIN_LEVEL = 0
NO_PATH_MARKER = "No Path"

def main():
    """Calling function for the recursive Floyd-Warshall algorithm."""
    recursive_floyd_warshall(MIN_LEVEL, MIN_LEVEL, MIN_LEVEL)
    # Print out the updated graph
    print_out_graph()

def print_out_graph():
    """
    This function prints out the graph with the distances
    and a placeholder for no path between nodes
    """
    for start_node in range(MAX_LENGTH):
        for end_node in range(MAX_LENGTH):
            distance = GRAPH[start_node][end_node]
            if distance == NO_PATH:
                distance = NO_PATH_MARKER

            message = f"Distance from Node {start_node} to Node {end_node} is {distance}"
            print(message)


def recursive_floyd_warshall(outer_loop: int, middle_loop: int, inner_loop: int):
    """
    This function computes shortest path between each pair node
    It computes by comparing a direct path with paths that have
    intermediate nodes in the path.

    The recursive path is the shortest path function which
    calls itself to find the shortest path between a pair of nodes

    Increment each variable until it reaches a loop

    :param outer_loop: This variable is from the first loop of the iterative version
    :param middle_loop: This variable is from the second loop of the iterative version
    :param inner_loop: This variable is from the last loop of the iterative version
    """

    if outer_loop >= MAX_LENGTH:
        return

    if middle_loop >= MAX_LENGTH:
        # Proceed to the next outer loop and reset middle/inner loops
        recursive_floyd_warshall(outer_loop + 1, MIN_LEVEL, MIN_LEVEL)
        return

    if inner_loop >= MAX_LENGTH:
        # Proceed to the next middle loop and reset the inner loop
        recursive_floyd_warshall(outer_loop, middle_loop + 1, MIN_LEVEL)
        return

    # Recursive case: compare direct path and path with intermediate node
    direct_path = GRAPH[middle_loop][inner_loop]
    path_with_intermediate = (
        GRAPH[middle_loop][outer_loop] + GRAPH[outer_loop][inner_loop]
        if GRAPH[middle_loop][outer_loop] != NO_PATH and GRAPH[outer_loop][inner_loop] != NO_PATH
        else NO_PATH
    )
    GRAPH[middle_loop][inner_loop] = min(direct_path, path_with_intermediate)

    # Continue with the next inner loop
    recursive_floyd_warshall(outer_loop, middle_loop, inner_loop + 1)


if __name__ == "__main__":
    main()
