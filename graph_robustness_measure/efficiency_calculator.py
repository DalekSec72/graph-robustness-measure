# -*- coding: utf-8 -*-

# 2020 HYU. CSE
# Taehun Kim <th6424@gmail.com>
# Hyein You <rkakrnl0@gmail.com>

import argparse

from graph_robustness_measure import graph
from graph_robustness_measure import floyd_warshall


# 플로이드 워셜 돌린 후 SP, second SP, ... 을 받아 E 계산.
def _sum_list_inverse(list):
    res = 0
    for i in list:
        if type(i) == type(list):
            res += _sum_list_inverse(i)
        else:
            if i != 0:
                res += 1 / i  # 역수로 바꿔 더해줌

    return res


def calculate_efficiency(costs, number_of_nodes):
    return 1 / (number_of_nodes * (number_of_nodes - 1)) * (_sum_list_inverse(costs[0]))


def calculate_efficiency_ssp(costs, number_of_nodes):
    return 2 / (3 * number_of_nodes * (number_of_nodes - 1)) * \
           (_sum_list_inverse(costs[0]) + _sum_list_inverse(costs[1]))


def main_read(file):
    g = graph.read_graph(file)
    costs = floyd_warshall.floyd(g)
    e_ssp = calculate_efficiency_ssp(costs, g.number_of_nodes())
    e_sp = calculate_efficiency(costs, g.number_of_nodes())

    file_name = file.split('/').pop()
    edgelist_path = f'../edgelists/{file_name}_{e_sp}_{e_ssp}.csv'
    fig_path = f'../graph_figures/{file_name}_{e_sp}_{e_ssp}.png'

    graph.write_graph(g, edgelist_path)
    graph.draw_graph(g, fig_path)


def main_new(args):
    def _isfloat(k):
        try:
            float(k)
            return True
        except ValueError:
            return False

    n = args[0]
    x = 0
    if len(args) > 1:
        if _isfloat(args[1]):
            x = args[1]
            graph_type = 'random'
        else:
            graph_type = args[1]

    if len(args) > 2:
        graph_type = args[2]

    print(n, x, graph_type, args[0], args[1])
    g = graph.generate_graph(n, x, graph_type)
    costs = floyd_warshall.floyd(g)
    e_ssp = calculate_efficiency_ssp(costs, g.number_of_nodes())
    e_sp = calculate_efficiency(costs, g.number_of_nodes())

    file_name = f'{graph_type}'
    edgelist_path = f'../edgelists/{file_name}_{n}_{x}_{e_sp}_{e_ssp}.csv'
    fig_path = f'../graph_figures/{file_name}_{n}_{x}_{e_sp}_{e_ssp}.png'

    graph.write_graph(g, edgelist_path)
    graph.draw_graph(g, fig_path)


def main():
    parser = argparse.ArgumentParser(description='Graph Efficiency Calculator')
    parser.set_defaults(func=lambda x: parser.print_usage())
    parser.add_argument('-r', '--read', metavar='FILE', help='Read edgelist file and calculate efficiency')
    parser.add_argument('-n', '--new',
                        metavar='NODE PROBABILITY GRAPH_TYPE',
                        nargs='*',
                        help='Generate random graph and calculate efficiency')

    args = parser.parse_args()

    if args.read:
        main_read(args.read)
    elif args.new:
        main_new(args.new)
    else:
        args.func(args)


if __name__ == '__main__':
    main()
