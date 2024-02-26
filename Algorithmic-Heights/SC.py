# Semi-Connected Graph
# https://rosalind.info/problems/sc/


from argparse import ArgumentParser

parser = ArgumentParser(description="name of the input file")
parser.add_argument(
    "-file", "--file_name", type=str, help="name of document with the example input"
)
args = parser.parse_args()


with open(f"./inputs/{args.file_name}", "r") as file:
    K = int(file.readline().strip())
    GRAPHS = []

    for line in file:
        if line.strip():
            node1, node2 = map(int, line.strip().split(" "))
            graph[node1].append(node2)
        else:
            V, E = map(int, file.readline().strip().split(" "))
            graph = {node + 1: [] for node in range(V)}
            GRAPHS.append(graph)

###############################################################################
import numpy as np

# the solution
# ==============================
def BFS(start_vertice, vertice, graph):
    quene, order = [], [] # quene存储需要进行遍历的数据， order存储遍历的路径
    distance = {i+1:0 for i in range(vertice)} # 初始化shortest path
    quene.append(start_vertice)
    order.append(start_vertice)
    # 进行广度优先遍历
    while quene:
        v = quene.pop(0)
        for n in graph[v]:
            if n not in order:
                distance[n] = distance[v] + 1
                order.append(n)
                quene.append(n)
    # 1无法到达的点，设置距离为-1
    for k in distance.keys():
        if k not in order:
            distance[k] = -1
    # 返回顺序，和距离
    return order, distance

def ifSemiConnectedGraph(graph, vertice):
    results = 1
    matrix = np.array([[0]*vertice for v in range(vertice)])
    for v in range(vertice):
        matrix[v][v] += 1

    for v in range(vertice):
        order, distance = BFS(v+1, vertice, graph)
        for k in distance.keys():
            if distance[k] != -1:
                matrix[v][k-1] += 1
                matrix[k-1][v] += 1
            else:
                matrix[v][k-1] -= 1
                matrix[k-1][v] -= 1
        matrix_flatten = matrix.flatten()
        if -2 in matrix_flatten:
            return -1
    return 1

for graph in GRAPHS:
    print(ifSemiConnectedGraph(graph, len(graph)))

###############################################################################


def Topological_Sorting(g: dict, n: set) -> list:
    graph, nodes = g.copy(), n.copy()
    output = []

    def indegree_node(thegraph, indgree=0):
        out_nodes = []
        for node1 in thegraph.keys():
            counter = 0
            for node2 in thegraph:
                if node1 in thegraph[node2]:
                    counter += 1
            if counter == indgree:
                out_nodes.append(node1)
        return out_nodes

    while indegree_node(graph) != []:
        output.extend(indegree_node(graph))
        for one in indegree_node(graph):
            graph.pop(one)
            nodes.remove(one)

    return output


################################################################################


# def boolsc(graph, reversegraph, numofnode):
#     for node in graph.keys():
#         if len(dfs(graph, node) | dfs(reversegraph, node)) < int(numofnode):
#             return -1
#     return 1


# def dfs(graph, node):
#     visited = set()
#     search(graph, node, visited)
#     return visited


# def search(graph, node, visited):
#     visited.add(node)
#     if node in graph:
#         for one in graph[node]:
#             if one not in visited:
#                 search(graph, one, visited)


# with open(f"./inputs/{args.file_name}") as f:
#     graphlist = []
#     edge = {}
#     reverseedge = {}
#     edgeflag = False
#     nodenum = []
#     for line in f:
#         if line.startswith("\n"):
#             continue
#         elif len(line.rstrip().split(" ")) == 2 and edgeflag == False:
#             if edge != {}:
#                 graphlist.append((edge, reverseedge))
#                 edgeflag = False
#             edge = {}  # start:ends
#             nodenum.append(line.rstrip().split(" ")[0])
#             tempedgenum = int(line.rstrip().split(" ")[1])
#             countedge = 0
#             edgeflag = True
#         elif len(line.rstrip().split(" ")) == 2 and edgeflag == True:
#             start, end = line.rstrip().split(" ")
#             if start not in edge:
#                 edge[start] = []
#             edge[start].append(end)
#             if end not in reverseedge:
#                 edge[end] = []
#             edge[end].append(start)
#             countedge += 1
#             if countedge == tempedgenum:
#                 edgeflag = False
#     graphlist.append((edge, reverseedge))

# for k in range(len(graphlist)):
#     print(boolsc(graphlist[k][0], graphlist[k][1], nodenum[k]), end=" ")

################################################################################


# def read_graph():
#     input()
#     n, e = map(int, input().split())
#     adjacent_lists = [[] for _ in range(n)]
#     edges = set()
#     for _ in range(e):
#         v1, v2 = map(int, input().split())
#         adjacent_lists[v1 - 1].append(v2 - 1)
#         edges.add((v1 - 1, v2 - 1))
#     return adjacent_lists, edges


# def search(adjacent_lists, visited, leave_sequences, tree_set, v):
#     visited[v] = True
#     for adj in adjacent_lists[v]:
#         if not visited[adj]:
#             search(adjacent_lists, visited, leave_sequences, tree_set, adj)
#     leave_sequences.append(v)
#     tree_set.add(v)


# def dfs(adjacent_lists, sources=None):
#     if sources == None:
#         sources = range(len(adjacent_lists))

#     visited = [False] * len(adjacent_lists)
#     leave_sequences = []
#     tree_sets = []
#     for source in sources:
#         if not visited[source]:
#             tree_set = set()
#             search(adjacent_lists, visited, leave_sequences, tree_set, source)
#             tree_sets.append(tree_set)
#     return leave_sequences, tree_sets


# def reverse_graph(adjacent_lists):
#     reversed_adjacent_lists = [[] for _ in range(len(adjacent_lists))]
#     for from_v in range(len(adjacent_lists)):
#         for to_v in adjacent_lists[from_v]:
#             reversed_adjacent_lists[to_v].append(from_v)
#     return reversed_adjacent_lists


# def find_strongly_connected_components(adjacent_lists):
#     leave_sequences = dfs(adjacent_lists)[0]
#     return dfs(reverse_graph(adjacent_lists), leave_sequences[::-1])[1]


# def has_edge_between(
#     edges, from_strongly_connected_component, to_strongly_connected_component
# ):
#     for from_v in from_strongly_connected_component:
#         for to_v in to_strongly_connected_component:
#             if (from_v, to_v) in edges:
#                 return True
#     return False


# def is_semi_connected(adjacent_lists, edges):
#     strongly_connected_components = find_strongly_connected_components(adjacent_lists)

#     for i in range(len(strongly_connected_components) - 1):
#         if not has_edge_between(
#             edges,
#             strongly_connected_components[i],
#             strongly_connected_components[i + 1],
#         ):
#             return False
#     return True


# def main():
#     k = int(input())
#     print(
#         " ".join(["1" if is_semi_connected(*read_graph()) else "-1" for _ in range(k)])
#     )


# if __name__ == "__main__":
#     main()


##############################################################################################

# Función EsSemiConectado(grafo):
#     Para cada vértice v en el grafo:
#         Si DFS(v) no alcanza todos los vértices y DFSReverso(v) no alcanza todos los vértices:
#             Retornar -1
#     Retornar 1

# Función DFS(v):
#     Marcar v como visitado
#     Para cada vértice adyacente w de v:
#         Si w no está marcado como visitado:
#             Llamar recursivamente DFS(w)

# Función DFSReverso(v):
#     Marcar v como visitado
#     Para cada vértice adyacente w de v en sentido contrario:
#         Si w no está marcado como visitado:
#             Llamar recursivamente DFSReverso(w)

# Para cada grafo en la lista de grafos:
#     Imprimir EsSemiConectado(grafo)
