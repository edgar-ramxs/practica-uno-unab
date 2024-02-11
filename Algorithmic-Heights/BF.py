# Bellman-Ford Algorithm
# https://rosalind.info/problems/bf/

# INFO:
# https://rosalind.info/glossary/algo-bellman-ford-algorithm/
# https://en.wikipedia.org/wiki/Bellman%E2%80%93Ford_algorithm

from argparse import ArgumentParser

parser = ArgumentParser(description="name of the input file")
parser.add_argument(
    "-file", "--file_name", type=str, help="name of document with the example input"
)
args = parser.parse_args()

with open(f"./inputs/{args.file_name}", "r") as file:
    NODOS, ARISTAS = map(int, file.readline().strip().split())
    GRAFO = {nodo + 1: [] for nodo in range(NODOS)}
    for line in file.readlines():
        nodo1, nodo2, peso = map(int, line.strip().split())
        GRAFO[nodo1].append((nodo2, peso))


def bellman_ford1(grafo: dict, origen: int = 1) -> str:
    distancias = {nodo: float("inf") for nodo in grafo}
    distancias[origen] = 0

    for _ in range(len(grafo) - 1):
        for nodo in grafo:
            for vecino, peso in grafo[nodo]:
                if (
                    distancias[nodo] != float("inf")
                    and distancias[nodo] + peso < distancias[vecino]
                ):
                    distancias[vecino] = distancias[nodo] + peso

    for nodo in grafo:
        for vecino, peso in grafo[nodo]:
            if (
                distancias[nodo] != float("inf")
                and distancias[nodo] + peso < distancias[vecino]
            ):
                distancias[vecino] = "x"

    output = ""
    for nodo, distancia in distancias.items():
        if distancia == float("inf"):
            output += f"x "
        else:
            output += f"{distancia} "

    return output


def bellman_ford2(grafo: dict, origen: int = 1) -> str:
    distancias = {nodo: float("inf") for nodo in grafo}
    distancias[origen] = 0

    for _ in range(len(grafo) - 1):
        for nodo_origen, adyacentes in grafo.items():
            for nodo_destino, peso in adyacentes:
                nueva_distancia = distancias[nodo_origen] + peso
                if nueva_distancia < distancias[nodo_destino]:
                    distancias[nodo_destino] = nueva_distancia

    for nodo_origen, adyacentes in grafo.items():
        for nodo_destino, peso in adyacentes:
            nueva_distancia = distancias[nodo_origen] + peso
            if nueva_distancia < distancias[nodo_destino]:
                return {nodo: "x" for nodo in grafo}

    output = ""
    for nodo, distancia in distancias.items():
        if distancia == float("inf"):
            output += f"x "
        else:
            output += f"{distancia} "

    return output


OUTPUT = bellman_ford1(GRAFO)
# OUTPUT = bellman_ford2(GRAFO)


with open(f"./outputs/output_{args.file_name}", "w") as output_file:
    output_file.write(OUTPUT)
