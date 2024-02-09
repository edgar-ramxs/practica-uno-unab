# Degree Array
# https://rosalind.info/problems/deg/

# Explicacion:
# El problema plantea que dado a las aristas de un grafo,
# se devuelta un array con los grados de los vertices ubicadolos en la poscion del vertice dentro del array.
#
#
# NOTA:
# primera linea, num de nodos - num de aristas
# Se puede optimizar en memoria y tiempo si se deja todo en una lista y se usa la funcion .count(node) para su grado en base de cuantas veces es mensionado en las aristas


from argparse import ArgumentParser

parser = ArgumentParser(description="name of the input file")
parser.add_argument(
    "-file", "--file_name", type=str, help="name of document with the example input"
)
args = parser.parse_args()

DEGREE_VERTEXS = {}
OUTPUT = ""


def counting_degree_vertex(node: int, dictionary=DEGREE_VERTEXS):
    if not node in dictionary:
        dictionary[node] = 1
    else:
        dictionary[node] += 1


with open(f"./inputs/{args.file_name}", "r") as file:
    nodes, edges = file.readline().strip().split(" ")
    for line in file:
        node1, node2 = line.strip().split(" ")
        counting_degree_vertex(int(node1))
        counting_degree_vertex(int(node2))


DEGREE_VERTEXS = sorted(DEGREE_VERTEXS.items())

for node, degree in DEGREE_VERTEXS:
    OUTPUT += f"{degree} "

with open(f"./outputs/output_{args.file_name}", "w") as output_file:
    output_file.write(OUTPUT)
