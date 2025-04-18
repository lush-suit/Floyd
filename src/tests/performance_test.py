"""
This module contains a simple performance test which
compares the recursive version of Floyd's algorithm with the
imperative version
"""

import sys
from time import process_time

sys.path.append('../')
from recursion.recursive_floyd import recursive_floyd_warshall, GRAPH as recursive_graph
from iterative.iterative_floyd import iterative_floyd, GRAPH as iterative_graph


def performance_test(function_handle, graph):
    """
    A function that performs a simple performance test

    :param function_handle: The function which is being tested.
                            It must take no parameters
    :param graph: The graph to use during the test
                  (to reset for each function execution).
    """
    # Reset the graph before running the function
    reset_graph(graph)

    # Measure start time
    start_time = process_time()

    # Call the function
    function_handle()

    # Measure end time
    end_time = process_time()

    # Calculate elapsed time
    elapsed_time = end_time - start_time

    print(f"Execution Time: {elapsed_time:.6f} seconds")  # Print timings


INITIAL_GRAPH_STATE = [
    [0, 7, sys.maxsize, 8],
    [sys.maxsize, 0, 5, sys.maxsize],
    [sys.maxsize, sys.maxsize, 0, 2],
    [sys.maxsize, sys.maxsize, sys.maxsize, 0],
]


def reset_graph(graph):
    """
       Resets the global GRAPH variable for the algorithm being tested to its initial state.
       """
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            graph[i][j] = INITIAL_GRAPH_STATE[i][j]


def test_recursive_floyd():
    recursive_floyd_warshall(0, 0, 0)

if __name__ == "__main__":
    print("Recursion Test Time")
    performance_test(test_recursive_floyd, recursive_graph)

    print("Iterative Test Time")
    performance_test(iterative_floyd, iterative_graph)
