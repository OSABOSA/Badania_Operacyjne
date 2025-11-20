import pandas as pd
from node import Node

def prepare_data(filename):
    with open(filename, "r") as f:
        first_line = f.readline().strip().split()
        N, M = int(first_line[0]), int(first_line[1])

        durations = list(map(int, f.readline().strip().split()))

        dep_line = f.readline().strip()
        dependencies = []
        for pair in dep_line.split("  "):
            if pair:
                a, b = map(int, pair.split(" "))
                dependencies.append((a - 1, b - 1))

    return N, M, durations, dependencies


def bellman_ford(N, nodes):
    for i in range(N):
        for node in nodes:
                node.EF = node.ES + node.t_oper
                for dep in node.d_outgoing:
                    dep.ES = max(dep.ES, node.EF)

    max_ef_node = max(nodes, key=lambda node: node.EF)

    critical_path = []
    current_node = max_ef_node
    while True:
        critical_path.append(current_node.id)
        if not current_node.d_incoming:
            break
        prev_node = max(current_node.d_incoming, key=lambda n: n.EF)
        current_node = prev_node

    critical_path.reverse()
    return critical_path, max_ef_node.EF


def cpm(N, nodes):
    for node in nodes:
        # chose whichever you like

        # node.EF = node.ES + node.t_oper
        # for anc in node.d_outgoing:
        #     anc.ES = max(anc.ES, node.EF)
        
        for pred in node.d_incoming:
            node.ES = max(node.ES, pred.EF)
        node.EF = node.ES + node.t_oper

    max_ef_node = max(nodes, key=lambda node: node.EF)

    critical_path = []
    current_node = max_ef_node
    while True:
        critical_path.append(current_node.id)
        if not current_node.d_incoming:
            break
        prev_node = max(current_node.d_incoming, key=lambda n: n.EF)
        current_node = prev_node

    critical_path.reverse()
    return critical_path, max_ef_node.EF


if __name__ == "__main__":

    for i in range(10, 81, 10):
        
        # for cpm has to be sorted
        filename = f"badania_operacyjne/cpm/data{i}.txt"
        filename = f"badania_operacyjne/cpm/dataSort{i}.txt"
        N, M, durations, dependencies = prepare_data(filename)
        nodes = Node.create_graph(N, M, durations, dependencies)
        bellman_ford(N, nodes)
        critical_path, process_time = cpm(N, nodes)
        
        print("Critical path:", critical_path)
        print("Process time:", process_time)

        # print("Number of tasks:", N)
        # print("Number of dependencies:", M)
        # print("Task durations:", durations)
        # print("Task dependencies:", dependencies)

