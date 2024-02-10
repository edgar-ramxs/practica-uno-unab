# Bellman-Ford Algorithm
# https://rosalind.info/problems/bf/

# INFO:
# https://rosalind.info/glossary/algo-bellman-ford-algorithm/

from argparse import ArgumentParser

parser = ArgumentParser(description="name of the input file")
parser.add_argument(
    "-file", "--file_name", type=str, help="name of document with the example input"
)
args = parser.parse_args()

with open(f"./inputs/{args.file_name}", "r") as file:
    NODOS, ARISTAS = map(int, file.readline().strip().split())
    GRAFO = {nodo + 1: [] for nodo in range(NODOS)}
    for line in file.readlines():
        nodo1, nodo2, peso = map(int, line.strip().split())
        GRAFO[nodo1].append((nodo2, peso))

print(NODOS)
print(ARISTAS)
print(GRAFO)


# with open(f"./outputs/output_{args.file_name}", "w") as output_file:
#   output_file.write(output)
