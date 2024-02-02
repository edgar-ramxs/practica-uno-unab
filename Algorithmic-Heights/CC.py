# Connected Components

from argparse import ArgumentParser

parser = ArgumentParser(description="name of the input file")
parser.add_argument(
    "-file", "--file_name", type=str, help="name of document with the example input"
)
args = parser.parse_args()

with open(f"./inputs/{args.file_name}", "r") as file:
    VERTICES, ARISTAS = list(map(int, file.readline().strip().split()))
    GRAFO = {v: [] for v in range(1, VERTICES + 1)}
    for line in file:
        node1, node2 = line.rsplit()
        # grado no dirigido
        GRAFO[int(node1)].append(int(node2))
        GRAFO[int(node2)].append(int(node1))


def connected_components(graph: dict = GRAFO) -> int:
    def dfs(vertex: int, visited: set) -> None:
        visited.add(vertex)
        for neighbor in graph.get(vertex, []):
            if neighbor not in visited:
                dfs(neighbor, visited)

    visited = set()
    components = 0

    for vertex in graph:
        if vertex not in visited:
            components += 1
            dfs(vertex, visited)

    return components


def connected_components2(graph: dict = GRAFO, nodes: int = VERTICES) -> int:
    def BFS(graph: dict, start: int, visited: list):
        stack = [start]
        visited[start] = True
        while stack:
            current_vertex = stack.pop()
            for neighbor in graph.get(current_vertex, []):
                if not visited[neighbor]:
                    stack.append(neighbor)
                    visited[neighbor] = True

    visited = [False] * (nodes + 1)
    components = 0
    for vertex in range(1, nodes + 1):
        if not visited[vertex]:
            components += 1
            BFS(graph, vertex, visited)

    return components


# print(connected_components())
# print(connected_components2())

output = str(connected_components())

with open(f"./outputs/output_{args.file_name}", "w") as output_file:
    output_file.write(output)
