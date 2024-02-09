# Binary Search
# https://rosalind.info/problems/bins/

# Explicacion:
# Existen dos listas A y B, conjutos con N e M que definen la cantidad de elementos guardados en las listas, respectivamente.
# Ahora, la tarea es encontrar la posicion o no de los elementos de la lista B posicionados dentro de la lista A.
# Si el elemento K dentro de B no existe en A, debe retornar -1, sino debiaria retornar 1.
#
#
# Notas:
# La lista A esta organizada de menor a mayor.
# Sin embargo, la lista B no necesariamente tiene un orden con relacion a sus elementos, ademas, existen repeticiones de los mismos.


from argparse import ArgumentParser

parser = ArgumentParser(description="name of the input file")
parser.add_argument(
    "-file", "--file_name", type=str, help="name of document with the example input"
)
args = parser.parse_args()

with open(f"./inputs/{args.file_name}", "r") as file:
    n, m, listA, listB = [line.rstrip() for line in file]
    A = list(map(int, listA.split(" ")))  # ListOrder
    B = list(map(int, listB.split(" ")))  # ListElement


# Usando una forma iterativa del algoritmo para evitar sobrecargar la pila de memoria
def binary_search(lista: list, k: int):
    start = 0
    middle = None
    end = len(lista) - 1

    while start <= end:
        middle = (start + end) // 2

        if lista[middle] < k:
            start = middle + 1

        elif lista[middle] > k:
            end = middle - 1

        else:
            return middle

    return -1


def searching_elements(ListOrder: list, ListElement: list):
    output = ""
    for k in ListElement:
        positionElement = binary_search(ListOrder, k)
        output += (
            f"{ positionElement + 1  if positionElement >= 0 else positionElement} "
        )
    return output


output = searching_elements(A, B)

with open(f"./outputs/output_{args.file_name}", "w") as output_file:
    output_file.write(str(output))
