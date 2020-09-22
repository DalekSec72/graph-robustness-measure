# -*- coding: utf-8 -*-

# 2020 HYU. CSE
# Taehun Kim <th6424@gmail.com>
# Hyein You <rkakrnl0@gmail.com>

import csv

from graph_robustness_measure import graph
from graph_robustness_measure import floyd_warshall
from graph_robustness_measure import efficiency_calculator


def repeat_test():
    gtypes = ['random', 'balanced_tree', 'cycle', 'star', 'wheel']

    for gtype in gtypes:
        with open(f'../{gtype}_graph_test.csv', 'w') as f:
            wr = csv.writer(f)
            for i in range(10):
                for nn in 10, 50, 100:
                    if gtype == 'random':
                        g = graph.generate_graph(n=nn, x=0.5, graph_type=gtype)
                    elif gtype == 'balanced_tree':
                        if nn == 100: break
                        g = graph.generate_graph(n=2, x=nn/10, graph_type=gtype)
                    else:
                        g = graph.generate_graph(n=nn, graph_type=gtype)

                    e_sp = efficiency_calculator.calculate_efficiency(floyd_warshall.floyd(g), g.number_of_nodes())
                    e_ssp = efficiency_calculator.calculate_efficiency_ssp(floyd_warshall.floyd(g), g.number_of_nodes())

                    wr.writerow([nn, i, e_sp, e_ssp])

                    edgelist_path = f'../edgelists/{gtype}_{nn}_{i}.csv'
                    picture_path = f'../graph_figures/{gtype}_{nn}_{i}.png'

                    graph.write_graph(g, edgelist_path)
                    print(f'{edgelist_path}')
                    graph.draw_graph(g, picture_path)
                    print(f'{picture_path}')


if __name__ == '__main__':
    repeat_test()