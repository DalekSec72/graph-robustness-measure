# -*- coding: utf-8 -*-

# 2020 HYU. CSE
# Taehun Kim <th6424@gmail.com>
# Hyein You <rkakrnl0@gmail.com>

import networkx as nx


# 엣지리스트 받아서 그래프 생성.
def make_graph_with_edgelist(edgelist):
    g = nx.Graph()
    g.add_edges_from(edgelist)
    return g

# 랜덤 그래프
def generate_random_graph(n, p):
    g = nx.gnp_random_graph(n, p)
    return g