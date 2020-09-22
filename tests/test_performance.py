# -*- coding: utf-8 -*-

# 2020 HYU. CSE
# Taehun Kim <th6424@gmail.com>
# Hyein You <rkakrnl0@gmail.com>

import time
import unittest
import networkx as nx
import csv

from graph_robustness_measure import graph
from graph_robustness_measure import floyd_warshall
from graph_robustness_measure import efficiency_calculator


# 작동시간 networkx 라이브러리 함수와 비교.
class PerformanceTests(unittest.TestCase):
    """
    def setUp(self):
        self.g = graph.generate_graph(1000, 0.5)
    """

    def test_floyd_warshall_performance(self):
        number_of_node = 500
        with open(f'../performance_{number_of_node}.csv', 'w') as f:
            wr = csv.writer(f)
            for i in range(1):
                g = graph.generate_graph(number_of_node, 0.5)

                start = time.time()
                floyd_warshall.floyd(g)
                t1 = time.time() - start

                start = time.time()
                nx.floyd_warshall(g)
                t2 = time.time() - start

                start = time.time()
                nx.floyd_warshall_numpy(g)
                t3 = time.time() - start

                wr.writerow([t1, t2, t3])

                print(t1, t2, t3)


    def test_efficiency_calculate_performance(self):
        start = time.time()
        floyd_result = floyd_warshall.floyd(self.g)
        efficiency_calculator.calculate_efficiency(floyd_result, self.g.number_of_nodes())
        t1 = time.time() - start

        start = time.time()
        nx.global_efficiency(self.g)
        t2 = time.time() - start

        print('efficiency calculate: ')
        print(t1, t2)


if __name__ == '__main__':
    unittest.main()
