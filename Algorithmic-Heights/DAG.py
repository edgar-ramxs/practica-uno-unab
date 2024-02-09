# DAG

# INFO
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




# def testing_acyclicity(grafos: list = GRAFOS) -> str:

#     def dfs(order: list, grafo: dict, vertice: int, visitados: list):
#         if visitados[vertice]:
#             order.append(vertice)
#             return True

#         visitados[vertice] = True
#         order.append(vertice)

#         for index in grafo[vertice]:
#             return dfs(order, grafo, index, visitados)
#         return False

#     def DAG(grafo: dict, vertices: int):
#         for nodo in range(1, vertices + 1):
#             visitados = [False for i in range(vertices + 1)]
#             order = []
#             if dfs(order, grafo, nodo, visitados):
#                 return -1
#         return 1

#     output = ""
#     for grafo in grafos:
#         resultado = DAG(grafo, len(grafo))
#         output += f"{resultado} "

#     return output





# def dfs(order, graph, v, visited):
#     # print(graph, v, visited)
#     if visited[v]:
#         order.append(v)
#         return True
#     visited[v] = True
#     order.append(v)

#     for i in graph[v]:
#         return(dfs(order, graph, i, visited))
#     return False

# def isDAG(graph, vertice):
#     for v in range(1, vertice+1):
#         visited = [False for i in range(int(vertice)+1)] # 记录该点是否被遍历过
#         order = [] # 记录遍历路径，如果路径回到某个点，说明有环

#         if dfs(order, graph, v, visited): #如果有环，输出-1；无环，输出1
#             # print(order)
#             # for o in order:
#             #     print(o, graph[o])
#             return(-1)

#     return(1)

# for n in range(len(GRAFOS)):
#     graph = GRAFOS[n]
#     vertice = len(graph)
#     print(isDAG(graph, vertice), end=" ")


# def es_aciclico(grafo: dict) -> bool:
#     def hay_ciclos(aristas: list, padre: int, grafo: dict) -> int:
#         if len(aristas) == 0:
#             return 1
#         for nodo in aristas:
#             if nodo == padre:
#                 return 1
#         for vertice in aristas:
#             return 0 + hay_ciclos(grafo[vertice], padre, grafo)

#     x = 0
#     for i in grafo:
#         x += hay_ciclos(grafo[i], i, grafo)
#     if x != 0:
#         print("El grafo contiene ciclos")
#     else:
#         print("El grafo es acíclico")


# def hay_ciclos(grafo: dict, vertice: int, visitados: set, padre: int) -> bool:
#     visitados.add(vertice)
#     for arista in grafo[vertice]:
#         print(arista)
#         if not arista in visitados:
#             if hay_ciclos(grafo, arista, visitados, vertice):
#                 return True
#         elif padre != arista:
#             return True
#     return False

# visitados = set()
# for vertice in grafo:
#     if not vertice in visitados:
#         if hay_ciclos(grafo, vertice, visitados, -1):
#             return True
# return False


# for index, grafo in enumerate(GRAFOS, start=1):
#     print(index, "->", grafo, "->", es_aciclico(grafo))
#     print()


# def is_cyclic_util(graph, vertex, visited, parent):
#     visited[vertex] = True
#     for neighbor in graph[vertex]:
#         if not visited[neighbor]:
#             if is_cyclic_util(graph, neighbor, visited, vertex):
#                 return True
#         elif parent != neighbor:
#             return True
#     return False

# def is_cyclic(graph):
#     num_vertices = len(graph)
#     visited = {vertex: False for vertex in graph}

#     for vertex in graph:
#         if not visited[vertex]:
#             if is_cyclic_util(graph, vertex, visited, -1):
#                 return True
#     return False

# for idx, graph in enumerate(GRAFOS, start=1):
#     if is_cyclic(graph):
#         print(f"Graph {idx} is cyclic.")
#     else:
#         print(f"Graph {idx} is acyclic.")
