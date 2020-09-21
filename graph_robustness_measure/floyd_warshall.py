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
    cost_ssp = [[INF for _ in range(number_of_nodes)] for _ in range(number_of_nodes)]

    # 연결된 edge의 코스트를 1로.
    for edge in edges:
        start, end = int(edge[0]), int(edge[1])
        cost[start][end] = 1

    for u in range(number_of_nodes):
        cost[u][u] = 0

    # 플로이드 워셜.
    for k in range(number_of_nodes):
        start_k = cost[k]
        for i in range(number_of_nodes):
            start_i = cost[i]
            start_i_ssp = cost_ssp[i]
            itok = cost[i][k]
            for j in range(number_of_nodes):
                # 더 짧은 경로로 변경.
                # 최단경로 변경시 second-sp 값에 기존 최단경로 값 입력
                # 그 외 버려지는 값일 경우 second-sp 값과 비교하여 더 낮은 값 입력
                itoj = start_i[j]
                distance = itok + start_k[j]
                itoj_ssp = start_i_ssp[j]

                if itoj > (distance):
                    start_i_ssp[j] = itoj
                elif itoj < (distance):
                    start_i_ssp[j] = min(itoj_ssp, distance)

                start_i[j] = cost[j][i] = min(itoj, distance)

            cost[i] = start_i
            cost_ssp[i] = start_i_ssp

        cost[k] = start_k

    result = [cost, cost_ssp]

    return cost
