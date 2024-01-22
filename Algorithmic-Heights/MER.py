# Merge Two Sorted Arrays

from argparse import ArgumentParser

parser = ArgumentParser(description="name of the input file")
parser.add_argument(
    "-file", "--file_name", type=str, help="name of document with the example input"
)
args = parser.parse_args()

with open(f"./inputs/{args.file_name}", "r") as file:
    N = int(file.readline().strip())
    A = list(map(int, file.readline().split()))
    M = int(file.readline().strip())
    B = list(map(int, file.readline().split()))

def Merge_Arrays(list1: list = A, list2: list = B) -> str:
    C = sorted(list1 + list2)
    return " ".join(map(str, C))

with open(f"./outputs/output_{args.file_name}", "w") as output_file:
    output_file.write(Merge_Arrays())