# BIP

from argparse import ArgumentParser

parser = ArgumentParser(description="name of the input file")
parser.add_argument(
    "-file", "--file_name", type=str, help="name of document with the example input"
)
args = parser.parse_args()

with open(f"./inputs/{args.file_name}", "r") as file:
    K = int(file.readline().strip())
    GRAFOS, vertices, aristas = [], [], []

    for line in file:
        if line.strip():
            l = list(map(int, line.strip().split(" ")))
            grafo[l[0]].append(l[1])
            grafo[l[1]].append(l[0])
        else:
            vertice, arista = map(int, file.readline().strip().split(" "))
            grafo = {i + 1: [] for i in range(vertice)}
            GRAFOS.append(grafo)
            vertices.append(vertice)
            aristas.append(arista)


def testing_bipartiteness(grafos: list = GRAFOS, k: int = K) -> str:

    def bip_test(grafo: dict, vertice: int, visitados: list, color: list) -> bool:
        for i in grafo[vertice]:
            if not visitados[i]:
                visitados[i] = True
                color[i] = not color[vertice]
                if not bip_test(grafo, i, visitados, color):
                    return False
            else:
                if color[vertice] == color[i]:
                    return False
        return True

    output = ""
    for i in range(k):
        graph = grafos[i]
        vertice = vertices[i]

        visitados = [False for i in range(vertice + 1)]
        color = [False for i in range(vertice + 1)]
        visitados[1] = True

        if bip_test(graph, 1, visitados, color):
            output += f"{1} "
        else:
            output += f"{-1} "
    return output


def testing_bipartiteness2(grafos: list = GRAFOS, k: int = K) -> str:
    output = ""

    def bip_test(grafo: dict) -> int:
        colors = {}
        for vertex in grafo:
            if vertex not in colors:
                colors[vertex] = 0
                queue = [vertex]
                front = 0
                while front < len(queue):
                    current_vertex = queue[front]
                    current_color = colors[current_vertex]
                    front += 1
                    for neighbor in grafo[current_vertex]:
                        if neighbor not in colors:
                            colors[neighbor] = 1 - current_color
                            queue.append(neighbor)
                        elif colors[neighbor] == current_color:
                            return -1
        return 1

    for grafo in grafos:
        resultado = bip_test(grafo)
        output += f"{resultado} "

    return output


with open(f"./outputs/output_{args.file_name}", "w") as output_file:
    output_file.write(testing_bipartiteness2())
