# Strongly Connected Components
# https://rosalind.info/problems/scc/


from argparse import ArgumentParser

parser = ArgumentParser(description="name of the input file")
parser.add_argument(
    "-file", "--file_name", type=str, help="name of document with the example input"
)
args = parser.parse_args()

with open(f"./inputs/{args.file_name}", "r") as file:
    V, E = map(int, file.readline().strip().split())
    GRAPH = {node + 1: [] for node in range(V)}

    for line in file.readlines():
        node1, node2 = map(int, line.strip().split())
        GRAPH[node1].append(node2)

    print(f"vertices: {V}, aristas: {E}")
    # print(f"grafo: {GRAPH}")
    print()


def SCC(graph: dict = GRAPH, vertices: int = V) -> list:

    def DFS(graph: dict, node: int, visited: list, SCCs: list):
        visited[node] = True
        SCCs.append(node)
        for i in graph[node]:
            if not visited[i]:
                DFS(graph, i, visited, SCCs)

    def fillOrder(node: int, visited: list, stack: list):
        visited[node] = True
        [fillOrder(i, visited, stack) for i in graph[node] if not visited[i]]
        stack.append(node)

    def getTranspose(graph: dict, vertices: int):
        return {
            v: [i for i in range(1, vertices + 1) if v in graph[i]]
            for v in range(1, vertices + 1)
        }

    stack = []
    visited = [False] * (vertices + 1)

    # PILA
    [fillOrder(ve, visited, stack) for ve in range(1, vertices + 1) if not visited[ve]]

    gr = getTranspose(graph, vertices)

    visited = [False] * (vertices + 1)
    SCCs = []

    while stack:
        i = stack.pop()
        if not visited[i]:
            DFS(gr, i, visited, SCCs)
            SCCs.append("")

    return SCCs.count("")


OUTPUT = f"{SCC()}"
with open(f"./outputs/output_{args.file_name}", "w") as output_file:
    output_file.write(OUTPUT)
