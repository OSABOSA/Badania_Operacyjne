from pert import prepare_data, probability_and_time
from node import Node
from cpm import cpm, bellman_ford
import numpy as np



if __name__ == "__main__":

    num_runs = 10000
    results = []

    # pert
    N, M, durations, dependencies, faster_than, probability_of_faster = prepare_data('badania_operacyjne/pert/pert_wzor.txt')
    nodes = Node.create_graph(N, M, durations, dependencies)
    critical_path, _ = bellman_ford(N, nodes)
    probability, est_time = probability_and_time(nodes, critical_path, faster_than, 50)

    # statistical
    for _ in range(num_runs):    
        for node in nodes:
            node.t_oper = np.random.uniform(node.duration[0], node.duration[2])
        critical_path, _ = cpm(N, nodes)
        _, time = cpm(N, nodes)
        results.append(time)
    average_result = np.average(results)

    # i have different outcome than I expected XDDDD
    print(f"Average result over {num_runs} runs: {average_result}")
    print(f"Probability of completing the project on time: {probability}")
    print(f"Expected time to complete the project: {est_time}")
