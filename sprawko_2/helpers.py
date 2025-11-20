import math
import heapq
from dijkstra import dijkstra
from bellman_ford import bellman_ford
from astar import astar

# ===============================
# --- Wczytywanie danych ---
# ===============================

def load_graph(path):
    with open(path, 'r') as f:
        raw = f.read().strip().split()
    N = int(raw[0])
    print(raw)
    nums = list(map(int, raw[1:N*N+1]))
    matrix = [nums[i*N:(i+1)*N] for i in range(N)]
    graph = {i: [] for i in range(N)}

    for i in range(N):
        for j in range(N):
            w = matrix[i][j]
            if w != 0:
                graph[i].append((j, w))
    return graph, N


# ==================================
# --- Pomocnicza rekonstrukcja drogi ---
# ==================================

def reconstruct_path(parent, v):
    if parent[v] is None:
        return [] if v != 0 else [0]
    path = []
    while v is not None:
        path.append(v)
        v = parent[v]
    return path[::-1]


# ===============================
# --- Funkcja wypisująca wynik ---
# ===============================

def print_results(dist, parent):
    for i, d in enumerate(dist):
        if d == math.inf:
            print("-1 []")
        else:
            print(d, reconstruct_path(parent, i))



# ===============================
# ----------- MAIN --------------
# ===============================

if __name__ == "__main__":
    graph, N = load_graph("badania_operacyjne/MinPaths/MinPaths_data5.txt")

    print("Dijkstra:")
    d, p = dijkstra(graph, N)
    print_results(d, p)
    print()

    print("Bellman-Ford:")
    d, p = bellman_ford(graph, N)
    print_results(d, p)
    print()

    print("A*:")
    d, p = astar(graph, N)
    print_results(d, p)
