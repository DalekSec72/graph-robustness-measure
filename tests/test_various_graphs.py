# -*- coding: utf-8 -*-

# 2020 HYU. CSE
# Taehun Kim <th6424@gmail.com>
# Hyein You <rkakrnl0@gmail.com>

import unittest

from graph_robustness_measure import graph
from graph_robustness_measure import floyd_warshall
from graph_robustness_measure import efficiency_calculator


class VariousGraphTests(unittest.TestCase):
    # 각 테스트마다 e값 넣어야함
    # binary
    def test_balanced_tree(self):
        g = graph.generate_graph(6, 3, graph_type='balanced_tree')
        r = floyd_warshall.floyd(g)
        e = efficiency_calculator.calculate_efficiency(r, g.number_of_nodes())
        e_ssp = efficiency_calculator.calculate_efficiency_ssp(r, g.number_of_nodes())

        path = '../example_tree_pic.png'
        graph.draw_graph(g, path)

        print(e)
        print(e_ssp)
        print('\n')

    def test_cycle_graph(self):
        g = graph.generate_graph(6, graph_type='cycle')
        r = floyd_warshall.floyd(g)
        e = efficiency_calculator.calculate_efficiency(r, g.number_of_nodes())
        e_ssp = efficiency_calculator.calculate_efficiency_ssp(r, g.number_of_nodes())

        path = '../example_cycle_pic.png'
        graph.draw_graph(g, path)

        print(e)
        print(e_ssp)
        print('\n')

    def test_star_graph(self):
        g = graph.generate_graph(6, graph_type='star')
        r = floyd_warshall.floyd(g)
        e = efficiency_calculator.calculate_efficiency(r, g.number_of_nodes())
        e_ssp = efficiency_calculator.calculate_efficiency_ssp(r, g.number_of_nodes())

        path = '../example_star_pic.png'
        graph.draw_graph(g, path)

        print(e)
        print(e_ssp)
        print('\n')

    def test_wheel_graph(self):
        g = graph.generate_graph(6, graph_type='wheel')
        r = floyd_warshall.floyd(g)
        e = efficiency_calculator.calculate_efficiency(r, g.number_of_nodes())
        e_ssp = efficiency_calculator.calculate_efficiency_ssp(r, g.number_of_nodes())

        path = '../example_wheel_pic.png'
        graph.draw_graph(g, path)

        print(e)
        print(e_ssp)
        print('\n')


if __name__ == '__main__':
    unittest.main()
