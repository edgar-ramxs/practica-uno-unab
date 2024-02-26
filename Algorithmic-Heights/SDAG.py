# Shortest Paths in DAG
# https://rosalind.info/problems/sdag/

# INFO:
#

from argparse import ArgumentParser

parser = ArgumentParser(description="name of the input file")
parser.add_argument(
    "-file", "--file_name", type=str, help="name of document with the example input"
)
args = parser.parse_args()


with open(f"./inputs/{args.file_name}", "r") as file:
    V, E = map(int, file.readline().strip().split())
    GRAPH = {node + 1: [] for node in range(V)}

    for line in file.readlines():
        node1, node2, weight = map(int, line.strip().split())
        GRAPH[node1].append((node2, weight))

    print(V, E)
    print(GRAPH)


# OUTPUT = ""
# with open(f"./outputs/output_{args.file_name}", "w") as output_file:
#     output_file.write(OUTPUT)
