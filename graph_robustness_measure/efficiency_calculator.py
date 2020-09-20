# -*- coding: utf-8 -*-

# 2020 HYU. CSE
# Taehun Kim <th6424@gmail.com>
# Hyein You <rkakrnl0@gmail.com>

from .graph import *
from .floyd_warshall import *


# 플로이드 워셜 돌린 후 SP, second SP, ... 을 받아 E 계산.
def sum_list_inverse(list):
    res = 0
    for i in list:
        if type(i) == type(list):
            res += sum_list_inverse(i)
        else:
            if i != 0:
                res += 1/i # 역수로 바꿔 더해줌

    return res

def calculate_efficiency(costs, number_of_nodes):
    efficiency = 1 / (number_of_nodes*(number_of_nodes-1)) * (sum_list_inverse(costs[0]))
    return efficiency

def calculate_efficiency_ssp(costs, number_of_nodes):
    efficiency = 2 / (3*number_of_nodes*(number_of_nodes-1)) * (sum_list_inverse(costs[0]) + 1/2*sum_list_inverse(costs[1]))

    return efficiency

if __name__ == '__main__':
    graph = make_graph_with_edgelist()
    costs = floyd(graph)
    e = calculate_efficiency(costs, graph.number_of_nodes())
    print(e)
