# Majority Element

# DOCUMENTATION:
#
# Algoritmo de Boyer-Moore
# https://es.wikipedia.org/wiki/Algoritmo_de_b%C3%BAsqueda_de_cadenas_Boyer-Moore
# https://www.geeksforgeeks.org/majority-element/

from argparse import ArgumentParser

parser = ArgumentParser(description="name of the input file")
parser.add_argument(
    "file_name", type=str, help="name of document with the example input"
)
args = parser.parse_args()

with open(f"./inputs/{args.file_name}", "r") as file:
    K, N = list(map(int, file.readline().strip().split()))
    Arrays = [list(map(int, line.rstrip().split(" "))) for line in file]


def majority_element_search(nums: list, n=N):
    candidate = None
    count = 0

    for num in nums:
        if count == 0:
            candidate = num
            count = 1
        elif candidate == num:
            count += 1
        else:
            count -= 1

    count = 0
    for num in nums:
        if num == candidate:
            count += 1

    if count > n // 2:
        return candidate
    else:
        return -1


output = ""
for A in Arrays:
    output += f"{majority_element_search(A)} "


with open(f"./outputs/output_{args.file_name}", "w") as output_file:
    output_file.write(output)
