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
            grafo[node1].append(node2)
        else:
            V, E = map(int, file.readline().strip().split(" "))
            grafo = {node + 1: [] for node in range(V)}
            GRAPHS.append(grafo)

print(GRAPHS)


# OUTPUT = ""
# with open(f"./outputs/output_{args.file_name}", "w") as output_file:
#     output_file.write(OUTPUT)
