import math
import heapq

# ===============================
# -------- BELLMAN-FORD ---------
# ===============================

def bellman_ford(graph, N, start=0):
    dist = [math.inf] * N
    parent = [None] * N
    dist[start] = 0

    for _ in range(N - 1):
        changed = False
        for u in graph:
            for v, w in graph[u]:
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    parent[v] = u
                    changed = True
        if not changed:
            break

    return dist, parent
