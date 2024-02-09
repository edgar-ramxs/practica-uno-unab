# Breadth-First Search
# https://rosalind.info/problems/bfs/

# INFO:
# https://rosalind.info/glossary/algo-breadth-first-search/

from argparse import ArgumentParser

parser = ArgumentParser(description="name of the input file")
parser.add_argument(
    "-file", "--file_name", type=str, help="name of document with the example input"
)
args = parser.parse_args()

with open(f"./inputs/{args.file_name}", "r") as file:
    VERTICES, EDGES = list(map(int, file.readline().strip().split()))
    GRAFO = {v: [] for v in range(1, VERTICES + 1)}

    for line in file:
        node1, node2 = line.rsplit()
        GRAFO[int(node1)].append(int(node2))
    # print(VERTICES, EDGES)
    # print(graph)


def Breadth_first_search(graph: dict = GRAFO, vertexes: int = VERTICES, start: int = 1) -> list:
    distances = [-1] * (vertexes + 1)
    distances[start] = 0
    queue = [start]

    while queue:
        current_vertex = queue.pop(0)
        for neighbor in graph.get(current_vertex, []):
            if distances[neighbor] == -1:
                distances[neighbor] = distances[current_vertex] + 1
                queue.append(neighbor)

    return distances[1:]


output = Breadth_first_search()
# print(output)

with open(f"./outputs/output_{args.file_name}", "w") as output_file:
    output_file.write(" ".join(map(str, output)))
