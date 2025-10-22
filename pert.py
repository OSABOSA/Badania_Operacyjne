import math
from scipy.stats import norm
from node import Node
from cpm import cpm, bellman_ford


def prepare_data(filename):
    with open(filename, "r", encoding="utf-8-sig") as f:
        first_line = f.readline().strip().split()
        N, M = int(first_line[0]), int(first_line[1])

        durations = []
        duration_line = f.readline().strip()
        for triple in duration_line.split("   "):
            t_min, t_avg, t_max = map(int, triple.split(" "))
            durations.append((t_min, t_avg, t_max))

        dependencies = []
        dep_line = f.readline().strip()
        for pair in dep_line.split("   "):
            a, b = map(int, pair.split(" "))
            dependencies.append((a - 1, b - 1))

        empty_line = f.readline()

        faster_than, probability_of_faster = map(int, f.readline().strip().split())
    return N, M, durations, dependencies, faster_than, probability_of_faster



def probability_and_time(nodes, critical_path, faster_than, probability_of_faster):
    time = 0
    var = 0
    for node_id in critical_path:
        node = nodes[node_id]
        time += node.t_oper
        var += node.var
    std_dev = var ** 0.5
    z = (faster_than - time) / std_dev if std_dev else math.inf #?? is it proper safety precaution
    probability = norm.cdf(z) * 100
    est_time = time + std_dev * norm.ppf(probability_of_faster / 100, loc=0, scale=std_dev)
    return probability, est_time



if __name__ == "__main__":

    N, M, durations, dependencies, faster_than, probability_of_faster = prepare_data('badania_operacyjne/pert/pert_wzor.txt')

    nodes = Node.create_graph(N, M, durations, dependencies)
    critical_path, _ = bellman_ford(N, nodes)
    probability, est_time = probability_and_time(nodes, critical_path, faster_than, probability_of_faster)

    print(f"Probability of completing the project faster than {faster_than}: {probability:.2f}%")
    print(f"Estimated project completion time: {est_time:.2f}")

