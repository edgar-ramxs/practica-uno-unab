# Variables and Some Arithmetic

from argparse import ArgumentParser

parser = ArgumentParser(description="name of the input file")
parser.add_argument(
    "file_name", type=str, help="name of document with the example input"
)
args = parser.parse_args()
elements = None

with open(f"./inputs/{args.file_name}", "r") as file:
    for line in file:
        elements = [element.rstrip() for element in line.split(" ")]

output = f"{(int(elements[0]) ** 2) + (int(elements[1]) ** 2)}"

with open(f"./outputs/output_{args.file_name}", "w") as output_file:
    output_file.write(output)


# VERSION BETA
#
# parser = ArgumentParser(
#     description="the square of the hypotenuse of the right triangle whose legs have lengths A and B"
# )
# parser.add_argument("A", type=int, help="cathetus A")
# parser.add_argument("B", type=int, help="cathetus B")
# args = parser.parse_args()
#
# C_square = (args.A**2) + (args.B**2)
# print(C_square)
