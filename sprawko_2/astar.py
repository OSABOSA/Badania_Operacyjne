import math
import heapq

# ===============================
# ----------- A* ----------------
# ===============================

# Heurystyka = 0 (masz brak współrzędnych) → A* działa jak Dijkstra
def zero_heuristic(a, b):
    return 0

def astar(graph, N, start=0):
    h = zero_heuristic
    dist = [math.inf] * N
    parent = [None] * N
    dist[start] = 0

    pq = [(0, start)]  # (f = g + h, node)

    while pq:
        f, u = heapq.heappop(pq)
        if f - h(u, 0) > dist[u]:
            continue

        for v, w in graph[u]:
            g_new = dist[u] + w
            if g_new < dist[v]:
                dist[v] = g_new
                parent[v] = u
                f_new = g_new + h(v, 0)
                heapq.heappush(pq, (f_new, v))

    return dist, parent


