# -*- coding: utf-8 -*-

# 2020 HYU. CSE
# Taehun Kim <th6424@gmail.com>
# Hyein You <rkakrnl0@gmail.com>

import unittest
import networkx as nx

from graph_robustness_measure import graph
from graph_robustness_measure import floyd_warshall
from graph_robustness_measure import efficiency_calculator


class VariousGraphTests(unittest.TestCase):
    # binary
    def balanced_tree_test(self):
        g = graph.generate_graph(2, 6, graph_type='balanced_tree')

#    def cycle_graph_test(self):

#    def star_graph_test(self):

#    def wheel_graph_test(self):


if __name__ == '__main__':
    unittest.main()