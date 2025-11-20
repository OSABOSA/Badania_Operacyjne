from collections import deque

def read_graph_from_file(filename):
    with open(filename, "r") as f:
        lines = [line.strip() for line in f if line.strip()]

    # Pierwsza linia: liczba wierzchołków
    n = int(lines[0])
    capacity = []

    # Kolejne n linii: macierz pojemności
    for i in range(1, 1 + n):
        row = list(map(int, lines[i].split()))
        capacity.append(row)

    return n, capacity


def bfs(capacity, flow, source, sink, parent):
    """ BFS znajduje ścieżkę powiększającą (Edmonds–Karp) """
    n = len(capacity)
    visited = [False] * n
    queue = deque([source])
    visited[source] = True
    parent[source] = -1

    while queue:
        u = queue.popleft()

        for v in range(n):
            if not visited[v] and capacity[u][v] - flow[u][v] > 0:
                queue.append(v)
                visited[v] = True
                parent[v] = u
                if v == sink:
                    return True

    return False


def max_flow(capacity, source=0, sink=None):
    n = len(capacity)
    if sink is None:
        sink = n - 1

    # Macierz przepływów
    flow = [[0] * n for _ in range(n)]
    parent = [-1] * n

    max_flow_value = 0
    augmenting_paths = []  # do wypisywania ścieżek

    while bfs(capacity, flow, source, sink, parent):
        # znajdź minimalną rezydualną pojemność na ścieżce
        path_flow = float('inf')
        v = sink
        path = []

        while v != source:
            u = parent[v]
            path_flow = min(path_flow, capacity[u][v] - flow[u][v])
            path.append(v)
            v = u

        path.append(source)
        path.reverse()

        augmenting_paths.append((path_flow, path))

        # aktualizacja przepływów
        v = sink
        while v != source:
            u = parent[v]
            flow[u][v] += path_flow
            flow[v][u] -= path_flow
            v = u

        max_flow_value += path_flow

    return max_flow_value, flow, augmenting_paths


def print_results(maxflow, flow, augmenting_paths):
    n = len(flow)

    print("\nMaksymalny przepływ:")
    print(maxflow)

    print("\nGraf przepływów:")
    for i in range(n):
        row = " ".join(str(flow[i][j]) for j in range(n))
        print(f"{sum(flow[i])} [{row}]")

    print("\nŚcieżki przepływów:")
    for amount, path in augmenting_paths:
        print(f"{amount} {path}")


# -----------------------------
# PRZYKŁADOWE URUCHOMIENIE
# -----------------------------

if __name__ == "__main__":
    filename = "badania_operacyjne/MaxFlows/MaxFlows_data5.txt"  # ← zmień na swoją nazwę
    n, capacity = read_graph_from_file(filename)

    maxflow, flow_matrix, augmenting_paths = max_flow(capacity)

    print_results(maxflow, flow_matrix, augmenting_paths)
