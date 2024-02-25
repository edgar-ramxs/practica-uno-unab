# 2-Satisfiability
# https://rosalind.info/problems/2sat/

# INFO:
# https://en.wikipedia.org/wiki/2-satisfiability
# https://codeforces.com/blog/entry/16205
# https://cp-algorithms.com/graph/2SAT.html
# https://www.geeksforgeeks.org/2-satisfiability-2-sat-problem/
# https://imada.sdu.dk/u/jbj/DM19/2SAT.pdf
# https://en.wikipedia.org/wiki/Kosaraju%27s_algorithm
# https://www.wikiwand.com/en/2-satisfiability


from argparse import ArgumentParser

parser = ArgumentParser(description="name of the input file")
parser.add_argument(
    "-file", "--file_name", type=str, help="name of document with the example input"
)
args = parser.parse_args()

################################################################################################


def dfs1_iterative(start_vertex, used, order, graph):
    stack = [start_vertex]
    while stack:
        v = stack.pop()
        if used[v]:
            continue
        used[v] = True
        order.append(v)
        for u in graph[v]:
            if not used[u]:
                stack.append(u)


def dfs2_iterative(start_vertex, cl, comp, graph_t):
    stack = [start_vertex]
    while stack:
        v = stack.pop()
        if comp[v] != -1:
            continue
        comp[v] = cl
        for u in graph_t[v]:
            if comp[u] == -1:
                stack.append(u)


def solve_2sat(n, graph, graph_t):
    order = []
    used = [False] * n
    for i in range(n):
        if not used[i]:
            dfs1_iterative(i, used, order, graph)

    comp = [-1] * n
    j = 0
    for i in range(n):
        v = order[n - i - 1]
        if comp[v] == -1:
            j += 1
            dfs2_iterative(v, j, comp, graph_t)

    assignment = [False] * (n // 2)
    for i in range(0, n, 2):
        if comp[i] == comp[i + 1]:
            print(0)
            return False
        assignment[i // 2] = comp[i] > comp[i + 1]

    print(1, end=" ")
    for i in range(len(assignment)):
        if assignment[i]:
            print(i + 1, end=" ")
        else:
            print(-(i + 1), end=" ")
    print()
    return True


if __name__ == "__main__":
    with open(f"./inputs/{args.file_name}", "r") as f:

        k = int(f.readline().strip())
        graphs, graphs_t, variables = [], [], []
        graph, graph_t = None, None

        for line in f:
            if line.strip():
                a, b = map(int, line.strip().split(" "))
                if a > 0 and b > 0:
                    graph[2 * abs(a) - 1].append(2 * abs(b) - 2)
                    graph[2 * abs(b) - 1].append(2 * abs(a) - 2)
                    graph_t[2 * abs(b) - 2].append(2 * abs(a) - 1)
                    graph_t[2 * abs(a) - 2].append(2 * abs(b) - 1)
                elif a < 0 and b > 0:
                    graph[2 * abs(a) - 2].append(2 * abs(b) - 2)
                    graph[2 * abs(b) - 1].append(2 * abs(a) - 1)
                    graph_t[2 * abs(b) - 2].append(2 * abs(a) - 2)
                    graph_t[2 * abs(a) - 1].append(2 * abs(b) - 1)
                elif a > 0 and b < 0:
                    graph[2 * abs(a) - 1].append(2 * abs(b) - 1)
                    graph[2 * abs(b) - 2].append(2 * abs(a) - 2)
                    graph_t[2 * abs(b) - 1].append(2 * abs(a) - 1)
                    graph_t[2 * abs(a) - 2].append(2 * abs(b) - 2)
                else:
                    graph[2 * abs(a) - 2].append(2 * abs(b) - 1)
                    graph[2 * abs(b) - 2].append(2 * abs(a) - 1)
                    graph_t[2 * abs(b) - 1].append(2 * abs(a) - 2)
                    graph_t[2 * abs(a) - 1].append(2 * abs(b) - 2)
            else:
                variable, _ = map(int, f.readline().strip().split(" "))
                variables.append(variable)
                graph = [[] for _ in range(2 * variable)]
                graphs.append(graph)
                graph_t = [[] for _ in range(2 * variable)]
                graphs_t.append(graph_t)

    for i in range(k):
        graph = graphs[i]
        graph_t = graphs_t[i]
        variable = variables[i]
        solve_2sat(variable * 2, graph, graph_t)


################################################################################################


# with open(f"./inputs/{args.file_name}", "r") as file:
#     K = int(file.readline().strip())
#     FORMULAS, INTANCES = [], []

#     for line in file:
#         if line.strip():
#             v1, v2 = map(int, line.strip().split(" "))
#             formula.append((v1, v2))
#         else:
#             VARIABLES, CLAUSES = map(int, file.readline().strip().split(" "))
#             formula = []
#             INTANCES.append((VARIABLES, CLAUSES))
#             FORMULAS.append(formula)


# from collections import defaultdict


# class TwoSAT:
#     def __init__(self, num_vars):
#         self.stack = []
#         self.scc_result = []
#         self.num_vars = num_vars
#         self.graph = defaultdict(list)
#         +1 to account for 0 index
#         self.scc = [-1] * (2 * num_vars + 1)
#         +1 to account for 0 index
#         self.visited = [False] * (2 * num_vars + 1)

#     def add_clause(self, var1, var2):
#         self.graph[-var1].append(var2)
#         self.graph[-var2].append(var1)

#     def dfs(self, u):
#         self.visited[u] = True
#         for v in self.graph[u]:
#             if not self.visited[v]:
#                 self.dfs(v)
#         self.stack.append(u)

#     def dfs_scc(self, u, scc_id):
#         self.visited[u] = False
#         self.scc[u] = scc_id
#         for v in self.graph[u]:
#             if self.visited[v]:
#                 self.dfs_scc(v, scc_id)

#     def satisfy_2sat(self):
#         for i in range(1, 2 * self.num_vars + 1):
#             if not self.visited[i]:
#                 self.dfs(i)

#         scc_id = 0
#         self.stack.reverse()
#         for u in self.stack:
#             if self.visited[u]:
#                 self.dfs_scc(u, scc_id)
#                 scc_id += 1

#         for i in range(1, self.num_vars + 1):
#             if self.scc[i] == self.scc[-i]:
#                 Unsatisfiable, no SCCs
#                 return None, []
#         assignment = [False] * self.num_vars
#         for i in range(1, self.num_vars + 1):
#             if self.scc[i] > self.scc[-i]:
#                 assignment[i - 1] = True

#         Gather SCCs
#         self.scc_result = [[] for _ in range(scc_id)]
#         for i in range(1, 2 * self.num_vars + 1):
#             self.scc_result[self.scc[i]].append(i)

#         return assignment, self.scc_result


# Example usage:
# if __name__ == "__main__":
#     for idx in range(K):
#         variables, clauses = INTANCES[idx]
#         sat_solver = TwoSAT(variables)

#         for V in FORMULAS[idx]:
#             x, y = V
#             sat_solver.add_clause(x, y)

#         assignment, sccs = sat_solver.satisfy_2sat()
#         if assignment:
#             print("Satisfiable. Assignment:", assignment)
#             print("Strongly Connected Components (SCCs):", sccs)
#         else:
#             print("Unsatisfiable.")

#         print()


################################################################################################
# OUTPUT = ""
# with open(f"./outputs/output_{args.file_name}", "w") as output_file:
#     output_file.write(OUTPUT)
