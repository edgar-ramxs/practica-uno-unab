# DAG
# https://rosalind.info/problems/dag/

# INFO:
# https://www.kaggle.com/code/bemc22/ordenamiento-topologico

from argparse import ArgumentParser

parser = ArgumentParser(description="name of the input file")
parser.add_argument(
    "-file", "--file_name", type=str, help="name of document with the example input"
)
args = parser.parse_args()

with open(f"./inputs/{args.file_name}", "r") as file:
    K = int(file.readline().strip())
    GRAFOS = []

    for line in file:
        if line.strip():
            node1, node2 = list(map(int, line.strip().split(" ")))
            grafo[node1].append(node2)  # Grafo Dirigido
        else:
            vertice, arista = map(int, file.readline().strip().split(" "))
            grafo = {i + 1: [] for i in range(vertice)}
            GRAFOS.append(grafo)


def testing_acyclicity(grafos: list = GRAFOS) -> str:

    def dfs(grafo: dict, vertice: int, visitados: list, en_proceso: list) -> bool:
        if visitados[vertice]:
            if vertice in en_proceso:
                return True
            return False

        visitados[vertice] = True
        en_proceso.append(vertice)

        for vecino in grafo[vertice]:
            if dfs(grafo, vecino, visitados, en_proceso):
                return True

        en_proceso.remove(vertice)
        return False

    def es_ciclico(grafo: dict, vertices: int) -> int:
        visitados = [False] * (vertices + 1)
        for nodo in range(1, vertices + 1):
            if dfs(grafo, nodo, visitados, []):
                return -1
        return 1

    output = ""
    for grafo in grafos:
        resultado = es_ciclico(grafo, len(grafo))
        output += f"{resultado} "

    return output


with open(f"./outputs/output_{args.file_name}", "w") as output_file:
    output_file.write(testing_acyclicity())
