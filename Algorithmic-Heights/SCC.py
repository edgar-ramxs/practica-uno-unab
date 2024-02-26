# Strongly Connected Components
# https://rosalind.info/problems/scc/

# INFO:
# https://www.geeksforgeeks.org/strongly-connected-components/
# https://en.wikipedia.org/wiki/Kosaraju%27s_algorithm
# https://gist.github.com/akueisara/120d8d5b4e1a663c606987b00e6c3c15
# https://es.wikipedia.org/wiki/Componente_fuertemente_conexo


from argparse import ArgumentParser

parser = ArgumentParser(description="name of the input file")
parser.add_argument(
    "-file", "--file_name", type=str, help="name of document with the example input"
)
args = parser.parse_args()

with open(f"./inputs/{args.file_name}", "r") as file:
    V, E = map(int, file.readline().strip().split())
    GRAPH = {node + 1: [] for node in range(V)}
    EDGES = []

    for line in file.readlines():
        node1, node2 = map(int, line.strip().split())
        GRAPH[node1].append(node2)
        EDGES.append((node1, node2))

    # print(f"vertices: {V}, aristas: {E}")
    # print(f"grafo: {GRAPH}")
    # print()


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


class Node:
    def __init__(self, value):
        self.value = value
        self.index = None
        self.lowlink = None
        self.on_stack = False
        self.neighbors = []  # List to store neighboring nodes

class Graph:
    def __init__(self):
        self.nodes = {}

    def add_edge(self, u, v):
        if u not in self.nodes:
            self.nodes[u] = Node(u)
        if v not in self.nodes:
            self.nodes[v] = Node(v)
        self.nodes[u].neighbors.append(self.nodes[v])  # Append the Node object

    def tarjan(self):
        index = 0
        stack = []
        scc = []
        scc_components = []

        def strong_connect(v):
            nonlocal index, stack, scc

            v.index = index
            v.lowlink = index
            index += 1
            stack.append(v)
            v.on_stack = True

            for neighbor in v.neighbors:
                if neighbor.index is None:
                    strong_connect(neighbor)
                    v.lowlink = min(v.lowlink, neighbor.lowlink)
                elif neighbor.on_stack:
                    v.lowlink = min(v.lowlink, neighbor.index)

            if v.lowlink == v.index:
                scc = []
                while stack:
                    w = stack.pop()
                    w.on_stack = False
                    scc.append(w.value)
                    if w == v:
                        break
                scc_components.append(scc)

        for node in self.nodes.values():
            if node.index is None:
                strong_connect(node)

        return scc_components


class GFG:
    # dfs Function to reach destination
    def dfs(self, curr, des, adj, vis):
        # If current node is the destination, return True
        if curr == des:
            return True
        vis[curr] = 1
        for x in adj[curr]:
            if not vis[x]:
                if self.dfs(x, des, adj, vis):
                    return True
        return False

    # To tell whether there is a path from source to destination
    def isPath(self, src, des, adj):
        vis = [0] * (len(adj) + 1)
        return self.dfs(src, des, adj, vis)

    # Function to return all the strongly connected components of a graph.
    def findSCC(self, n, a):
        # Stores all the strongly connected components.
        ans = []

        # Stores whether a vertex is a part of any Strongly Connected Component
        is_scc = [0] * (n + 1)

        adj = [[] for _ in range(n + 1)]

        for i in range(len(a)):
            adj[a[i][0]].append(a[i][1])

        # Traversing all the vertices
        for i in range(1, n + 1):
            if not is_scc[i]:
                # If a vertex i is not a part of any SCC, insert it into a new SCC list
                # and check for other vertices whether they can be part of this list.
                scc = [i]
                for j in range(i + 1, n + 1):
                    # If there is a path from vertex i to vertex j and vice versa,
                    # put vertex j into the current SCC list.
                    if (
                        not is_scc[j]
                        and self.isPath(i, j, adj)
                        and self.isPath(j, i, adj)
                    ):
                        is_scc[j] = 1
                        scc.append(j)
                # Insert the SCC containing vertex i into the final list.
                ans.append(scc)
        return ans


# Driver Code Starts
if __name__ == "__main__":
    # Example usage
    graph = Graph()

    for edge in EDGES:
        graph.add_edge(edge[0], edge[1])

    scc_components = graph.tarjan()
    print("Strongly connected components:")
    print(len(scc_components))

# obj = GFG()
# ans = obj.findSCC(V, EDGES)
# print("Strongly Connected Components are:")
# print(len(ans))


# This code is contributed by shivamgupta310570


# OUTPUT = f"{SCC()}"
# with open(f"./outputs/output_{args.file_name}", "w") as output_file:
#     output_file.write(OUTPUT)
