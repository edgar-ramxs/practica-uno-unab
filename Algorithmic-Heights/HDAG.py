# Hamiltonian Path in DAG
# https://rosalind.info/problems/hdag

# INFO:
# https://networkx.org/documentation/stable/reference/algorithms/generated/networkx.algorithms.tournament.hamiltonian_path.html


from argparse import ArgumentParser

parser = ArgumentParser(description="name of the input file")
parser.add_argument(
    "-file", "--file_name", type=str, help="name of document with the example input"
)
args = parser.parse_args()


with open(f"./inputs/{args.file_name}", "r") as file:
    K = int(file.readline().strip())
    GRAPHS, VERTEXES, EDGES = [], [], []

    for line in file:
        if line.strip():
            node1, node2 = list(map(int, line.strip().split(" ")))
            graph[node1].append(node2)
        else:
            V, E = map(int, file.readline().strip().split(" "))
            graph = {node + 1: [] for node in range(V)}
            GRAPHS.append(graph)
            VERTEXES.append(V)
            EDGES.append(E)


def hamiltonian_path(G: list = GRAPHS, V: list = VERTEXES, k: int = K) -> str:

    def topologicalsortUtil(v: int, visited: list, path: list) -> None:
        visited[v] = True
        for i in graph[v]:
            if visited[i] == False:
                topologicalsortUtil(i, visited, path)
        path.insert(0, v)

    def topologicalsort(graph: dict, vertice: int) -> list:
        visited = [False] * (vertice + 1)
        path = []
        for v in range(1, vertice + 1):
            if visited[v] == False:
                topologicalsortUtil(v, visited, path)
        return path

    def check_consecutive(path: list, graph: dict) -> bool:
        for i in range(len(path) - 1):
            if path[i + 1] not in graph[path[i]]:
                return False
        return True

    # Hamiltonian Path in DAG => OUTPUT
    output = ""
    for n in range(k):
        graph = G[n]
        vertice = V[n]
        path = topologicalsort(graph, vertice)
        if check_consecutive(path, graph):
            output += f"{1} {' '.join(map(str, path))}\n"
        else:
            output += f"{-1}\n"

    return output


# ARREGLAR
# def hamiltonian_path(G: list = GRAPHS, V: list = VERTEXES, k: int = K) :

#     def topological_sort_and_check(graph: dict, vertice: int) -> tuple[bool, list]:
#         path = []
#         visited = set()

#         def explore(v: int) -> None:
#             if v in visited:
#                 return
#             visited.add(v)
#             for neighbor in graph[v]:
#                 explore(neighbor)
#             path.append(v)

#         for v in range(1, vertice + 1):
#             if v not in visited:
#                 explore(v)

#         return check_consecutive(path, graph), path

#     def check_consecutive(path: list, graph: dict) -> bool:
#         for i, v in enumerate(path[:-1]):
#             if path[i + 1] not in graph[v]:
#                 return False
#         return True

#     for n in range(k):
#         graph = G[n]
#         vertice = V[n]
#         is_hamiltonian, path = topological_sort_and_check(graph, vertice)
#         yield f"{1 if is_hamiltonian else -1} {' '.join(map(str, path))}\n"


OUTPUT = hamiltonian_path()
with open(f"./outputs/output_{args.file_name}", "w") as output_file:
    output_file.write(OUTPUT)
