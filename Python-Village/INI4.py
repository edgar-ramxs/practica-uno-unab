# Conditions and Loops
# https://rosalind.info/problems/ini4/

from argparse import ArgumentParser

parser = ArgumentParser(description="name of the input file")
parser.add_argument(
    "-file", "--file_name", type=str, help="name of document with the example input"
)
args = parser.parse_args()

with open(f"./inputs/{args.file_name}", "r") as file:
    A, B = list(map(int, file.readline().strip().split()))

OUTPUT = f"{sum(num for num in range(A, B) if num % 2 == 1)}"

with open(f"./outputs/output_{args.file_name}", "w") as output_file:
    output_file.write(OUTPUT)
