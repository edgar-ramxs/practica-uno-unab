# Strings and Lists

from argparse import ArgumentParser

parser = ArgumentParser(description="name of the input file")
parser.add_argument(
    "file_name", type=str, help="name of document with the example input"
)
args = parser.parse_args()
elements = []

with open(f"./inputs/{args.file_name}", "r") as file:
    for line in file:
        elements += [element.rstrip() for element in line.split(" ")]

# print(elements) | str int int int int
TEXT = elements[0]
A = int(elements[1])
B = int(elements[2])
C = int(elements[3])
D = int(elements[4])

output = f"{TEXT[A:B+1]} {TEXT[C:D+1]}"

with open(f"./outputs/output_{args.file_name}", "w") as output_file:
    output_file.write(output)


# VERSION BETA
#
# from argparse import ArgumentParser
#
# parser = ArgumentParser(description="The slice of this string")
# parser.add_argument("TEXT", type=str, help="text")
# parser.add_argument("A", type=int, help="A")
# parser.add_argument("B", type=int, help="B")
# parser.add_argument("C", type=int, help="C")
# parser.add_argument("D", type=int, help="D")
#
# args = parser.parse_args()  # Objects Namespace | cannot be decomposed
#
# output = f"{args.TEXT[args.A:args.B+1]} {args.TEXT[args.C:args.D+1]}"
# print(output)
