# Shortest Cycle Through a Given Edge
# https://rosalind.info/problems/cte/

# INFO:
# https://es.wikipedia.org/wiki/Algoritmo_de_Floyd-Warshall

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
            nodo1, nodo2, peso = map(int, line.strip().split(" "))
            grafo[nodo1].append((nodo2, peso))  # Grafo Dirigido
        else:
            vertice, arista = map(int, file.readline().strip().split(" "))
            grafo = {i + 1: [] for i in range(vertice)}
            GRAFOS.append(grafo)


for grafo in GRAFOS:
    print(grafo)


def Shortest_Cycle_Through_a_Given_Edge(grafo: dict, nodo: int):
    distancias = {vertice: float("inf") for vertice in grafo}
    predecesor = {vertice: None for vertice in grafo}

    return


# #####################################################

# import numpy as np
# import sys

# # the input:
# # A positive integer k≤20 and k simple directed graphs with positive integer edge weights and at most 10**3 vertices in the edge list format
# # ==============================
# data = "./inputs/rosalind_cte.txt"

# graphs = []  # 存储所有的graphs
# vertices = []  # 存储所有的graphs的顶点数目
# edges = []  # 存储所有的graphs的边数目
# first_specified_edges = []
# # 读取数据,有向图
# with open(data, "r") as f:
#     k = int(f.readline().strip())

#     for line in f:
#         # print(line)
#         if len(line.strip().split(" ")) == 3:
#             vertice1, vertice2, weight = list(map(int, line.strip().split(" ")))
#             graph[vertice1][vertice2] = weight

#         else:
#             # 获得顶点和边
#             vertice, edge = map(int, f.readline().strip().split(" "))
#             # 获得每个顶点的邻居点
#             graph = {v: {} for v in range(1, vertice + 1)}
#             graphs.append(graph)
#             vertices.append(vertice)
#             edges.append(edge)
#             first_specified_edges.append(
#                 list(map(int, f.readline().strip().split(" ")))
#             )

# print(graphs)
# print(vertices)
# print(edges)
# print(first_specified_edges)

# def BellmanFord(graph, vertice, source):
#     # 初始化
#     distance = {i: sys.maxsize for i in graph}  # 初始设置为代表无穷大
#     predecessor = {i: None for i in graph}
#     distance[source] = 0  # 到原点距离设置为0

#     # 对每一条边重复操作
#     for i in range(vertice - 1):
#         for u in graph:
#             if distance[u] != sys.maxsize:
#                 for v in graph[u]:
#                     if distance[v] > distance[u] + graph[u][v]:
#                         distance[v] = distance[u] + graph[u][v]
#                         predecessor[v] = u

#     # 检查是否有负权重的边
#     for u in graph:
#         if distance[u] != sys.maxsize:
#             for v in graph[u]:
#                 if distance[v] > distance[u] + graph[u][v]:
#                     print("with negative cycles")

#     return distance, predecessor


# # the results:
# for n in range(k):
#     graph = graphs[n]
#     vertice = vertices[n]
#     first_specified_edge = first_specified_edges[n]
#     distance, predecessor = BellmanFord(graph, vertice, first_specified_edge[1])
#     if distance[first_specified_edge[0]] == sys.maxsize:
#         print(-1, end=" ")
#     else:
#         print(distance[first_specified_edge[0]] + first_specified_edge[2], end=" ")
# print(distance)

# print()
# print(graphs)
# print(vertices)
# print(edges)
# print(first_specified_edges[0])

#####################################################

# def dfs(graph, node):
#     visited = set()
#     search(graph, node, visited)
#     return visited


# def search(graph, node, visited):
#     visited.add(node)
#     for theedge in graph.keys():
#         if theedge[0] == node:
#             if theedge[1] not in visited:
#                 search(graph, theedge[1], visited)


# def cte(graph, specialedge):
#     # the distance from the end node 'e' to start node 's' of the special edge , Bellman_Ford
#     s, e = specialedge[0], specialedge[1]
#     downnodes = dfs(graph, specialedge[1])
#     if s not in downnodes:
#         return -1
#     # init
#     d = {}
#     inf = 1000000000000
#     for node in downnodes:
#         d[node] = graph[(e, node)] if (e, node) in graph else inf
#     # compute
#     for m in range(len(downnodes)):
#         for edge in graph.keys():
#             if edge[0] in downnodes and edge[1] in downnodes:
#                 # relax
#                 if d[edge[1]] > d[edge[0]] + graph[edge]:
#                     d[edge[1]] = d[edge[0]] + graph[edge]
#     return d[s] + graph[specialedge]


# with open("./inputs/rosalind_cte.txt") as f:
#     graphlist = []
#     edge = {}
#     for line in f:
#         if len(line.rstrip().split(" ")) == 2:
#             nodenum = int(line.rstrip().split(" ")[0])
#             if edge != {}:
#                 graphlist.append((edge, firstedge))
#             edge = {}
#         elif len(line.rstrip().split(" ")) == 3:
#             start, end, length = line.rstrip().split(" ")
#             if edge == {}:
#                 firstedge = (start, end)
#             edge[(start, end)] = int(length)
#     graphlist.append((edge, firstedge))

# for one in graphlist:
#     print(cte(*one), end=" ")
# print()


##################################################

# with open(f"./outputs/output_{args.file_name}", "w") as output_file:
#     output_file.write()
