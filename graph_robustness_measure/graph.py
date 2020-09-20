# -*- coding: utf-8 -*-

# 2020 HYU. CSE
# Taehun Kim <th6424@gmail.com>
# Hyein You <rkakrnl0@gmail.com>


import matplotlib.pyplot as plt
import networkx as nx


# 엣지리스트 받아서 그래프 생성.
def make_graph_with_edgelist(edgelist):
    g = nx.Graph()
    g.add_edges_from(edgelist)
    return g


# default 랜덤 그래프, 타입 지정해주면 해당 타입 생성.
def generate_graph(n, x, graph_type='random'):
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
    g = nx.gnp_random_graph(n, p)
    return g


# balanced_tree
def generate_balanced_tree(n, h):
    g = nx.balanced_tree(n, h)
    return g


# cycle_graph
def generate_cycle_graph(n):
    g = nx.cycle_graph(n)
    return g


# star_graph
def generate_star_graph(n):
    g = nx.star_graph(n)
    return g


# wheel_graphs
def generate_wheel_graph(n):
    g = nx.wheel_graph(n)
    return g


def draw_graph(g):
    # 테스트 못해봄
    nx.draw(g)
    plt.savefig('graph.png')
    plt.show()


def write_graph(g, name):
    nx.write_edgelist(g, name)
