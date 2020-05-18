# -*- coding: utf-8 -*-

# 2020 HYU. CSE
# Taehun Kim <th6424@gmail.com>
# Hyein You <rkakrnl0@gmail.com>

import networkx as nx

#example
edgelist = [(1, 2), (1, 3)]

#엣지리스트 받아서 그래프 생성.
def make_graph_with_edgelist(edgelist):
    g = nx.Graph()
    g.add_edges_from(edgelist)
    return g