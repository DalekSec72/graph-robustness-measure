# -*- coding: utf-8 -*-

# 2020 HYU. CSE
# Taehun Kim <th6424@gmail.com>
# Hyein You <rkakrnl0@gmail.com>


import matplotlib.pyplot as plt
import networkx as nx


# default 랜덤 그래프, 타입 지정해주면 해당 타입 생성.
def generate_graph(n, x=0, graph_type='random'):
    n = int(n)
    try:
        if graph_type == 'random':
            return nx.gnp_random_graph(n, float(x))
        elif graph_type == 'balanced_tree':
            return nx.balanced_tree(n, int(x))
        elif graph_type == 'cycle':
            return nx.cycle_graph(n)
        elif graph_type == 'star':
            return nx.star_graph(n)
        elif graph_type == 'wheel':
            return nx.wheel_graph(n)
        else:
            raise Exception('Not supporting type')
    except Exception as e:
        print(e)


def draw_graph(g, path):
    plt.cla()
    nx.draw(g)
    plt.savefig(path)
    # plt.show()


def read_graph(path):
    return nx.read_edgelist(path)


def write_graph(g, path):
    nx.write_edgelist(g, path)
