# -*- coding: utf-8 -*-

# 2020 HYU. CSE
# Taehun Kim <th6424@gmail.com>
# Hyein You <rkakrnl0@gmail.com>


import matplotlib.pyplot as plt
import networkx as nx


# default 랜덤 그래프, 타입 지정해주면 해당 타입 생성.
def generate_graph(n, x=0, graph_type='random'):
    try:
        if graph_type == 'random':
            return generate_random_graph(n, x)
        elif graph_type == 'balanced_tree':
            return generate_balanced_tree(n, x)
        elif graph_type == 'cycle':
            return generate_cycle_graph(n)
        elif graph_type == 'star':
            return generate_star_graph(n)
        elif graph_type == 'wheel':
            return generate_wheel_graph(n)
        else:
            raise Exception('Not supporting type')
    except Exception as e:
        print(e)


# 랜덤 그래프
def generate_random_graph(n, p):
    return nx.gnp_random_graph(n, p)


# balanced_tree
def generate_balanced_tree(n, h):
    return nx.balanced_tree(n, h)


# cycle_graph
def generate_cycle_graph(n):
    return nx.cycle_graph(n)


# star_graph
def generate_star_graph(n):
    return nx.star_graph(n)


# wheel_graph
def generate_wheel_graph(n):
    return nx.wheel_graph(n)


def draw_graph(g, path):
    plt.cla()
    nx.draw(g)
    plt.savefig(path)
    #plt.show()


def read_graph(path):
    return nx.read_edgelist(path)


def write_graph(g, path):
    nx.write_edgelist(g, path)
