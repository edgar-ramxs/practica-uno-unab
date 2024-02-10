# Square in a Graph
# https://rosalind.info/problems/sq/

# INFO:
# https://rosalind.info/glossary/algo-simple-graph/
# https://www.geeksforgeeks.org/cycles-of-length-n-in-an-undirected-and-connected-graph/

from argparse import ArgumentParser

parser = ArgumentParser(description="name of the input file")
parser.add_argument(
    "-file", "--file_name", type=str, help="name of document with the example input"
)
args = parser.parse_args()

with open(f"./inputs/{args.file_name}", "r") as file:
    K = int(file.readline().strip())
    GRAFOS, VERTICES, ARISTAS = [], [], []

    for line in file:
        if line.strip():
            nodo1, nodo2 = list(map(int, line.strip().split(" ")))
            k_grafos = len(GRAFOS) - 1
            GRAFOS[k_grafos][nodo1 - 1][nodo2 - 1] = 1
            GRAFOS[k_grafos][nodo2 - 1][nodo1 - 1] = 1
        else:
            vertice, arista = map(int, file.readline().strip().split(" "))
            matriz = [[0] * vertice for _ in range(vertice)]
            GRAFOS.append(matriz)
            VERTICES.append(vertice)
            ARISTAS.append(arista)


def countCycles1(graph: list, length_cycle: int):

    def DFS(graph: list, marked: list, n: int, vert: int, start: int, count: int):
        marked[vert] = True

        if n == 0:
            marked[vert] = False
            if graph[vert][start] == 1:
                count = count + 1
                return count
            else:
                return count

        for i in range(len(graph)):
            if marked[i] == False and graph[vert][i] == 1:
                count = DFS(graph, marked, n - 1, i, start, count)

        marked[vert] = False
        return count

    count = 0
    marked = [False] * len(graph)

    for i in range(len(graph) - (length_cycle - 1)):
        count = DFS(graph, marked, length_cycle - 1, i, i, count)
        marked[i] = True

    if (count / 2) > 0:
        return 1
    return -1


output = ""
for grafo in GRAFOS:
    output += f"{countCycles1(grafo, 4)} "


with open(f"./outputs/output_{args.file_name}", "w") as output_file:
    output_file.write(output)
