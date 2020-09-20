# -*- coding: utf-8 -*-


import unittest
import networkx as nx

from graph_robustness_measure import graph
from graph_robustness_measure import floyd_warshall
from graph_robustness_measure import efficiency_calculator


# 함수들 작동 여부만 테스트하는 basic tests.
class FloydWarshallTests(unittest.TestCase):
    def test_floyd(self):
        g = graph.generate_graph(100, 0.5)
        r = floyd_warshall.floyd(g)
        nx_r = nx.floyd_warshall_numpy(g)

        self.assertListEqual(r[0], nx_r.tolist())

    def test_sum_list_inverse(self):
        sample_list = [[2, 5, 20], [0, floyd_warshall.INF]]
        expected = 15 / 20
        actual = efficiency_calculator.sum_list_inverse(sample_list)

        self.assertAlmostEqual(actual, expected)

    def test_calculate_efficiency(self):
        g = graph.generate_graph(100, 0.5)
        r = floyd_warshall.floyd(g)
        e = efficiency_calculator.calculate_efficiency(r, g.number_of_nodes())
        nx_e = nx.global_efficiency(g)

        self.assertEqual(e, nx_e)

    def test_calculate_efficiency_ssp(self):
        g = graph.generate_graph(100, 0.5)
        r = floyd_warshall.floyd(g)
        e_ssp = efficiency_calculator.calculate_efficiency_ssp(r, g.number_of_nodes())

        self.assertLessEqual(e_ssp, 1)


if __name__ == '__main__':
    unittest.main()
