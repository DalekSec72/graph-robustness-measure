# -*- coding: utf-8 -*-


import unittest
from graph_robustness_measure import graph
from graph_robustness_measure import floyd_warshall


class FloydWarshallTests(unittest.TestCase):
    def test_floyd(self):
        g = graph.generate_random_graph(5, 0.7)
        r = floyd_warshall.floyd(g)
        sp = r[0]
        s_sp = r[1]
        print(g.edges)
        print(sp)
        print(s_sp)



if __name__ == '__main__':
    unittest.main()
