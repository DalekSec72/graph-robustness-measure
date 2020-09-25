# -*- coding: utf-8 -*-

# 2020 HYU. CSE
# Taehun Kim <th6424@gmail.com>
# Hyein You <rkakrnl0@gmail.com>

import sys
import networkx as nx
import operator

from graph_robustness_measure import graph
from graph_robustness_measure import floyd_warshall
from graph_robustness_measure import efficiency_calculator


def remove_high_betweenness_edges(g):
    betweenness = nx.edge_betweenness_centrality(g)
    target_edge = sorted(betweenness.items(), key=operator.itemgetter(1)).pop()  # tuple
    print(target_edge)
    g.remove_edge(*target_edge[0])
    return g


if __name__ == '__main__':
    g = graph.read_graph(sys.argv[1])
    for _ in range(5):
        g = remove_high_betweenness_edges(g)

    costs = floyd_warshall.floyd(g)

    e_ssp = efficiency_calculator.calculate_efficiency_ssp(costs, g.number_of_nodes())
    e_sp = efficiency_calculator.calculate_efficiency(costs, g.number_of_nodes())

    path = f'{sys.argv[1]}_removed_{e_sp}_{e_ssp}.csv'
    graph.write_graph(g, path)
