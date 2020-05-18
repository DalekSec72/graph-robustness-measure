# -*- coding: utf-8 -*-

# 2020 HYU. CSE
# Taehun Kim <th6424@gmail.com>
# Hyein You <rkakrnl0@gmail.com>

from .graph import *

INF: float = float('inf')

# 그래프를 받아 플로이드 워셜 알고리즘 작동 후 SP와 second SP..(인접행렬 형태)를 반환.
def floyd(graph):
    number_of_nodes = graph.number_of_nodes()
    number_of_edges = graph.number_of_edges()

    # initialize
    for i in range(number_of_nodes):
        for j in range(number_of_nodes):
            if i == j:
                arr[i][j] = 0
            else:
                arr[i][j] = INF
