# Double-Degree Array

from argparse import ArgumentParser

parser = ArgumentParser(description="name of the input file")
parser.add_argument(
    "file_name", type=str, help="name of document with the example input"
)
args = parser.parse_args()
degree_neighbors = {}
output = ""


def counting_degree_vertex(node1: int, node2: int, dictionary=degree_neighbors):
    if not node1 in dictionary:
        dictionary[node1] = [1, node2]
    else:
        dictionary[node1][0] += 1
        dictionary[node1].append(node2)


with open(f"./inputs/{args.file_name}", "r") as file:
    nodes, edges = list(map(int, file.readline().strip().split()))
    for line in file:
        node1, node2 = tuple(map(int, line.rstrip().split()))
        counting_degree_vertex(node1, node2)
        counting_degree_vertex(node2, node1)


for node in range(1, nodes + 1):
    count = 0
    if not node in degree_neighbors:
        output += f"0 "
    else:
        for neighbors in degree_neighbors[node][1:]:
            count += degree_neighbors[neighbors][0]
        output += f"{count} "


with open(f"./outputs/output_{args.file_name}", "w") as output_file:
    output_file.write(str(output))
