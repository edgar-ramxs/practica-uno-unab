# General Sink
# https://rosalind.info/problems/gs/


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


def find_reachable_vertex(graph):
    for vertex in graph:
        reachable = set()
        stack = [vertex]

        while stack:
            current_vertex = stack.pop()
            reachable.add(current_vertex)

            for neighbor in graph[current_vertex]:
                if neighbor not in reachable:
                    stack.append(neighbor)

        if len(reachable) == len(graph):
            return vertex

    return -1


# print(GRAPHS)
output = ''
for graph in GRAPHS:
    # print(graph)
    result = find_reachable_vertex(graph)
    output += f'{result} '
    # print(result)

with open(f"./outputs/output_{args.file_name}", "w") as output_file:
    output_file.write(output)
