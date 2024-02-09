# Merge Sort
# https://rosalind.info/problems/ms/

# INFO:
# https://medium.com/@tudorache.a.bogdan/divide-and-conquer-merge-sort-59b6e5ebe1db

from argparse import ArgumentParser

parser = ArgumentParser(description="name of the input file")
parser.add_argument(
    "-file", "--file_name", type=str, help="name of document with the example input"
)
args = parser.parse_args()

with open(f"./inputs/{args.file_name}", "r") as file:
    N = int(file.readline().strip())
    A = list(map(int, file.readline().split()))


def merge_sort(array: list):
    if len(array) > 1:
        mitad = len(array) // 2

        izquierda = array[:mitad]
        derecha = array[mitad:]

        merge_sort(izquierda)
        merge_sort(derecha)

        i = j = k = 0

        while i < len(izquierda) and j < len(derecha):
            if izquierda[i] < derecha[j]:
                array[k] = izquierda[i]
                i += 1
            else:
                array[k] = derecha[j]
                j += 1
            k += 1

        while i < len(izquierda):
            array[k] = izquierda[i]
            i += 1
            k += 1

        while j < len(derecha):
            array[k] = derecha[j]
            j += 1
            k += 1


merge_sort(A)

with open(f"./outputs/output_{args.file_name}", "w") as output_file:
    output_file.write(" ".join(map(str, A)))
