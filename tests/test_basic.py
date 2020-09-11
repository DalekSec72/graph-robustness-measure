# -*- coding: utf-8 -*-


import unittest
from graph_robustness_measure import graph
from graph_robustness_measure import floyd_warshall
from graph_robustness_measure import efficiency_calculator


class FloydWarshallTests(unittest.TestCase):
    def test_floyd(self):
        g = graph.generate_random_graph(5, 0.7)
        r = floyd_warshall.floyd(g)

        sp = r[0]
        s_sp = r[1]
        print(g.edges)
        print(sp)
        print(s_sp)

    def test_sum_list_inverse(self):
        sample_list = [[2, 5, 20], [0, floyd_warshall.INF]]
        expected = 15/20
        actual = efficiency_calculator.sum_list_inverse(sample_list)

        self.assertAlmostEqual(actual, expected)

    def test_calculate_efficiency(self):
        g = graph.generate_random_graph(5, 1)
        r = floyd_warshall.floyd(g)
        e = efficiency_calculator.calculate_efficiency(r, g.number_of_nodes())

        print(g.edges)
        print(r[0])
        print(r[1])
        print(e)

        self.assertLessEqual(e, 1)


if __name__ == '__main__':
    unittest.main()
