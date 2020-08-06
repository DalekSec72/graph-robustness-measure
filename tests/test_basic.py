# -*- coding: utf-8 -*-


import unittest
from graph_robustness_measure import graph
from graph_robustness_measure import floyd_warshall


class FloydWarshallTests(unittest.TestCase):
    def test_floyd(self):
        g = graph.generate_random_graph(5, 0.7)
        print(g.edges)
        print(floyd_warshall.floyd(g))



if __name__ == '__main__':
    unittest.main()
