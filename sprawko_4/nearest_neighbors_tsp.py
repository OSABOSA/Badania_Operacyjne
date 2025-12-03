import math
import os


def load_tsp_from_file(filename):
    nodes = {}
    is_coord_section = False

    if not os.path.exists(filename):
        print(f"ERROR: File '{filename}' not found.")
        return None

    try:
        with open(filename, 'r') as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue

                if "NODE_COORD_SECTION" in line:
                    is_coord_section = True
                    continue

                if line == "EOF":
                    break

                if is_coord_section:
                    parts = line.split()
                    if len(parts) >= 3:
                        try:
                            node_id = int(parts[0])
                            x = float(parts[1])
                            y = float(parts[2])
                            nodes[node_id] = (x, y)
                        except ValueError:
                            continue

        return nodes
    except Exception as e:
        print(f" FILE ERROR: {e}")
        return None


def calculate_distance(node1, node2):
    return math.sqrt((node1[0] - node2[0]) ** 2 + (node1[1] - node2[1]) ** 2)


def tsp_nearest_neighbor(nodes):

    if not nodes:
        return [], 0.0

    unvisited = set(nodes.keys())

    start_node = min(nodes.keys())
    current_node = start_node

    path = [current_node]
    unvisited.remove(current_node)
    total_distance = 0.0

    while unvisited:
        nearest_node = None
        min_dist = float('inf')

        for candidate in unvisited:
            dist = calculate_distance(nodes[current_node], nodes[candidate])
            if dist < min_dist:
                min_dist = dist
                nearest_node = candidate

        if nearest_node is not None:
            path.append(nearest_node)
            unvisited.remove(nearest_node)
            total_distance += min_dist
            current_node = nearest_node

    return_dist = calculate_distance(nodes[current_node], nodes[start_node])
    path.append(start_node)
    total_distance += return_dist

    return path, total_distance


if __name__ == "__main__":
    FILE_NAME = 'data/tsp48.tsp'

    print(f"--- Rozwiązywanie TSP (Nearest Neighbor) ---")
    print(f"Wczytywanie z pliku: {FILE_NAME}...")

    coords = load_tsp_from_file(FILE_NAME)

    if coords:
        print(f"Pomyślnie wczytano {len(coords)} miast.")

        route, distance = tsp_nearest_neighbor(coords)

        print("\n=== WYNIKI ===")
        print(f"Trasa: {route}")
        print(f"Długość trasy: {distance:.2f}")
    else:
        print("ERROR.")