# Dijkstra's Algorithm
# https://rosalind.info/problems/dij/

# INFO:
# https://www6.uniovi.es/usr/cesar/Uned/EDA/Apuntes/TAD_apUM_07.pdf
# https://es.wikipedia.org/wiki/Grafo_ponderado
# https://es.wikipedia.org/wiki/Algoritmo_de_Dijkstra
# http://algorithmics.lsi.upc.edu/docs/Dasgupta-Papadimitriou-Vazirani.pdf

from argparse import ArgumentParser

parser = ArgumentParser(description="name of the input file")
parser.add_argument(
    "-file", "--file_name", type=str, help="name of document with the example input"
)
args = parser.parse_args()

with open(f"./inputs/{args.file_name}", "r") as file:
    NODES, EDGES = map(int, file.readline().strip().split())
    GRAFO = {node + 1: [] for node in range(NODES)}
    for line in file.readlines():
        node1, node2, weight = map(int, line.strip().split())
        GRAFO[node1].append((node2, weight))


def dijkstra1(grafo: dict = GRAFO, nodo_origen: int = 1) -> str:
    distancias = {nodo: float("inf") for nodo in grafo}
    distancias[nodo_origen] = 0
    visitados = set()

    while visitados != set(grafo):
        nodo_actual = min(
            (nodo for nodo in distancias if nodo not in visitados), key=distancias.get
        )
        visitados.add(nodo_actual)

        for vecino, peso in grafo[nodo_actual]:
            if vecino not in visitados:
                nueva_distancia = distancias[nodo_actual] + peso
                if nueva_distancia < distancias[vecino]:
                    distancias[vecino] = nueva_distancia

    output = ""
    for nodo, distancia in distancias.items():
        if distancia == float("inf"):
            output += "-1 "
        else:
            output += f"{distancia} "
    return output


def dijkstra2(grafo: dict = GRAFO, nodo_origen: int = 1) -> str:
    distancias = {nodo: float("inf") for nodo in grafo}
    distancias[nodo_origen] = 0
    visitados = set()
    heap = [(0, nodo_origen)]

    while heap:
        min_dist = float("inf")
        min_vertice = None
        for dist, vertice in heap:
            if dist < min_dist and vertice not in visitados:
                min_dist = dist
                min_vertice = vertice

        if min_vertice is None:
            break

        heap.remove((min_dist, min_vertice))
        visitados.add(min_vertice)

        for vecino, peso in grafo[min_vertice]:
            if vecino not in visitados:
                nueva_distancia = min_dist + peso
                if nueva_distancia < distancias[vecino]:
                    distancias[vecino] = nueva_distancia
                    heap.append((nueva_distancia, vecino))

    output = ""
    for nodo, distancia in distancias.items():
        if distancia == float("inf"):
            output += "-1 "
        else:
            output += f"{distancia} "
    return output


OUTPUT = dijkstra2()

with open(f"./outputs/output_{args.file_name}", "w") as output_file:
    output_file.write(OUTPUT)
