# -*- coding: utf-8 -*-

# 2020 HYU. CSE
# Taehun Kim <th6424@gmail.com>
# Hyein You <rkakrnl0@gmail.com>

INF: float = float('inf')


# 그래프를 받아 플로이드 워셜 알고리즘 작동 후 SP와 second SP..(인접행렬 형태)를 반환.
def floyd(graph):
    number_of_nodes = graph.number_of_nodes()
    edges = graph.edges()

    # 무한대로 초기화.
    cost = [[INF for _ in range(number_of_nodes)] for _ in range(number_of_nodes)]

    # 연결된 edge의 코스트를 1로.
    for edge in edges:
        start, end = edge[0], edge[1]
        cost[start][end] = 1

    # 플로이드 워셜.
    for k in range(number_of_nodes):
        for i in range(number_of_nodes):
            for j in range(number_of_nodes):
                # 자기 자신은 0.
                if i == j:
                    cost[i][j] = 0
                # 더 짧은 경로로 변경.
                else:
                    cost[i][j] = min(cost[i][j], cost[i][k] + cost[k][j])

    return cost

