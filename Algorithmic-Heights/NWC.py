# Negative Weight Cycle
# https://rosalind.info/problems/nwc/

from argparse import ArgumentParser

parser = ArgumentParser(description="name of the input file")
parser.add_argument(
    "-file", "--file_name", type=str, help="name of document with the elamdaample input"
)
args = parser.parse_args()


with open(f"./inputs/{args.file_name}", "r") as file:
    K = int(file.readline().strip())
    GRAPHS, VERTICES, EDGES = [], [], []

    for line in file:
        data = list(map(int, line.rstrip().split(" ")))

        if len(data) == 3:
            node1, node2, weight = data
            graph[node1].append((node2, weight))

        elif len(data) == 2:
            V, E = data
            graph = {node + 1: [] for node in range(V)}
            GRAPHS.append(graph)

            # VERTICES.append(V)
            # EDGES.append(E)


def bellman_ford(graph: dict) -> int:
    for source in graph:
        distances = {vertex: float("inf") for vertex in graph}
        distances[source] = 0
        changed = True

        # Relax edges repeatedly
        for _ in range(len(graph) - 1):
            if not changed:
                break
            changed = False
            for u in graph:
                for v, weight in graph[u]:
                    if (
                        distances[u] != float("inf")
                        and distances[u] + weight < distances[v]
                    ):
                        distances[v] = distances[u] + weight
                        changed = True

        # Check for negative weight cycle
        for u in graph:
            for v, weight in graph[u]:
                if (
                    distances[u] != float("inf")
                    and distances[u] + weight < distances[v]
                ):
                    return 1  # Negative weight cycle detected

    return -1


output = ""
for graph in GRAPHS:
    is_negative_weight_cycle = bellman_ford(graph)
    output += f"{is_negative_weight_cycle} "


with open(f"./outputs/output_{args.file_name}", "w") as output_file:
    output_file.write(output)
