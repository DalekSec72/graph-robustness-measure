# -*- coding: utf-8 -*-

# 2020 HYU. CSE
# Taehun Kim <th6424@gmail.com>
# Hyein You <rkakrnl0@gmail.com>

import os
import unittest
import networkx as nx

from graph_robustness_measure import graph
from graph_robustness_measure import floyd_warshall
from graph_robustness_measure import efficiency_calculator


# 함수들 정상 작동 여부 테스트하는 basic tests.
class FloydWarshallTests(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(FloydWarshallTests, self).__init__(*args, **kwargs)
        self.g = graph.generate_graph(5, 0.5)
        self.r = floyd_warshall.floyd(self.g)

    def test_floyd(self):
        nx_r = nx.floyd_warshall_numpy(self.g)

        self.assertListEqual(self.r[0], nx_r.tolist())

    def test_floyd_dict(self):
        nx_r = nx.floyd_warshall(self.g)
        r = floyd_warshall.floyd_dict(self.g)

        self.assertDictEqual(r, nx_r)

    def test_floyd_dict_ssp(self):
        r = floyd_warshall.floyd_dict(self.g)[1]

        self.assertDictEqual(r, self.r[1])

    def test_calculate_efficiency(self):
        e = efficiency_calculator.calculate_efficiency(self.r, self.g.number_of_nodes())
        nx_e = nx.global_efficiency(self.g)

        self.assertEqual(e, nx_e)

    def test_calculate_efficiency_ssp(self):
        e_ssp = efficiency_calculator.calculate_efficiency_ssp(self.r, self.g.number_of_nodes())

        self.assertLessEqual(e_ssp, 1)

    # 그래프 저장 후 다시 읽어서 같으면 패스.
    def test_write_read_graph(self):
        path = '../example_graph.csv'
        graph.write_graph(self.g, path)
        read_graph = graph.read_graph(path)

        self.assertIs(nx.is_isomorphic(self.g, read_graph), True)

    def test_draw_graph(self):
        path = '../example_graph_pic.png'
        graph.draw_graph(self.g, path)

    def tearDown(self):
        ex_graph = '../example_graph.csv'
        ex_pic = '../example_graph_pic.png'
        try:
            os.remove(ex_graph)
            os.remove(ex_pic)
        except OSError:
            pass


if __name__ == '__main__':
    unittest.main()
