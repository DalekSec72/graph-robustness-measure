# -*- coding: utf-8 -*-

# 2020 HYU. CSE
# Taehun Kim <th6424@gmail.com>
# Hyein You <rkakrnl0@gmail.com>

import os, sys
# os.environ["MATPLOTLIBDATA"] = os.path.join(sys._MEIPASS, "mpl-data")
os.environ["MATPLOTLIBDATA"] = os.path.join(os.path.split(sys.executable)[0], "Lib/site-packages/matplotlib/mpl-data")

import matplotlib.pyplot as plt
import networkx as nx

# 엣지리스트 받아서 그래프 생성.
def make_graph_with_edgelist(edgelist):
    g = nx.Graph()
    g.add_edges_from(edgelist)
    return g

def make_graph_with_type(type, n, x):
    if type=='random':
        return generate_random_graph(n, x);
    elif type=='balanced_tree':
        return generate_balanced_tree(n, x);
    elif type=='cycle':
        return generate_cycle_graph(n);
    elif type=='star':
        return generate_star_graph(n);
    elif type=='wheel':
        return generate_wheel_graph(n);
    else:
        return generate_random_graph(n, x);

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
    g = nx.gnp_cycle_graph(n)
    return g

# star_graph
def generate_star_graph(n):
    g = nx.gnp_star_graph(n)
    return g

# wheel_graphs
def generate_wheel_graph(n):
    g = nx.gnp_wheel_graph(n)
    return g

def draw_graph(g):
    # 테스트 못해봄
    nx.draw(g)
    plt.savefig('graph.png')
    plt.show()

def write_graph(g, name):
    nx.write_edgelist(g, name)
