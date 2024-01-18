# Insertion Sort

# DOCUMENTATION:
#
# https://www.toptal.com/developers/sorting-algorithms/insertion-sort
# https://en.wikipedia.org/wiki/Insertion_sort

from argparse import ArgumentParser

parser = ArgumentParser(description="name of the input file")
parser.add_argument(
    "file_name", type=str, help="name of document with the example input"
)
args = parser.parse_args()

with open(f"./inputs/{args.file_name}", "r") as file:
    n = int(file.readline().strip())
    A = list(map(int, file.readline().strip().split()))


def insertion_sort(n_elements: int, array: list):
    swap = 0
    for i in range(1, n_elements):
        j = i
        while j > 0 and array[j] < array[j - 1]:
            array[j], array[j - 1] = array[j - 1], array[j]
            swap += 1
            j -= 1
    return swap


output = insertion_sort(n, A)

with open(f"./outputs/output_{args.file_name}", "w") as output_file:
    output_file.write(str(output))
