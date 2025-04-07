import unittest
from iterative_floyd import iterative_floyd, print_out_graph, GRAPH as iterative_graph
from recursive_floyd import recursive_floyd_warshall, print_out_graph as recursive_print, GRAPH as recursive_graph
import sys


class TestFloydWarshall(unittest.TestCase):

    def setUp(self):
        """Reset the graph to its initial state for every test."""
        self.initial_state = [
            [0, 7, sys.maxsize, 8],
            [sys.maxsize, 0, 5, sys.maxsize],
            [sys.maxsize, sys.maxsize, 0, 2],
            [sys.maxsize, sys.maxsize, sys.maxsize, 0],
        ]
        self.reset_graph(iterative_graph)
        self.reset_graph(recursive_graph)

    def reset_graph(self, graph):
        """Helper function to reset the graph."""
        for i in range(len(graph)):
            for j in range(len(graph[i])):
                graph[i][j] = self.initial_state[i][j]

    def test_iterative_floyd(self):
        """Test the correctness of the iterative Floyd-Warshall algorithm."""
        iterative_floyd()
        expected_result = [
            [0, 7, 12, 8],
            [sys.maxsize, 0, 5, 7],
            [sys.maxsize, sys.maxsize, 0, 2],
            [sys.maxsize, sys.maxsize, sys.maxsize, 0],
        ]
        self.assertEqual(iterative_graph, expected_result)

    def test_recursive_floyd(self):
        """Test the correctness of the recursive Floyd-Warshall algorithm."""
        recursive_floyd_warshall(0, 0, 0)
        expected_result = [
            [0, 7, 12, 8],
            [sys.maxsize, 0, 5, 7],
            [sys.maxsize, sys.maxsize, 0, 2],
            [sys.maxsize, sys.maxsize, sys.maxsize, 0],
        ]
        self.assertEqual(recursive_graph, expected_result)

    def test_output_format(self):
        """Test the output format of the print function."""
        from io import StringIO
        import sys

        # Capture the output of the iterative version
        output = StringIO()
        sys.stdout = output
        print_out_graph()
        iterative_output = output.getvalue()

        # Capture the output of the recursive version
        output = StringIO()
        sys.stdout = output
        recursive_print()
        recursive_output = output.getvalue()

        self.assertEqual(iterative_output, recursive_output)

    def test_empty_graph(self):
        """Test the algorithm with an empty graph."""
        empty_graph = []
        self.reset_graph(empty_graph)  # Reset graph to empty state
        iterative_floyd()
        self.assertEqual(empty_graph, [])  # Should remain empty

    def test_large_graph(self):
        """Test the algorithm with a large graph."""
        large_graph = [[0 if i == j else sys.maxsize for j in range(100)] for i in range(100)]
        self.assertIsNone(iterative_floyd())  # Ensure it runs without errors

    def test_consistency_between_versions(self):
        """Ensure iterative and recursive versions produce identical results."""
        iterative_floyd()
        iterative_result = [row[:] for row in iterative_graph]  # Copy the output

        self.reset_graph(recursive_graph)  # Reset recursive graph
        recursive_floyd_warshall(0, 0, 0)
        self.assertEqual(iterative_result, recursive_graph)


if __name__ == '__main__':
    unittest.main()
