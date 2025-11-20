import math
import heapq

# ===============================
# -------- DIJKSTRA -------------
# ===============================

def dijkstra(graph, N, start=0):
    dist = [math.inf] * N
    parent = [None] * N
    dist[start] = 0
    pq = [(0, start)]

    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue

        for v, w in graph[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                parent[v] = u
                heapq.heappush(pq, (dist[v], v))

    return dist, parent

