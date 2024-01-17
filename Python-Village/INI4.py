# Conditions and Loops

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

output = (
    f"{sum(num for num in range(int(elements[0]), int(elements[1])) if num % 2 == 1)}"
)

with open(f"./outputs/output_{args.file_name}", "w") as output_file:
    output_file.write(output)


# VERSION BETA
#
# from argparse import ArgumentParser
#
# parser = ArgumentParser(description="The sum of all odd integers")
# parser.add_argument("starting", type=int, help="num to starting the loop")
# parser.add_argument("ending", type=int, help="num to ending the loop")
# args = parser.parse_args()
#
# count = 0
# for num in range(args.starting, args.ending):
#     if num % 2 == 1:
#         count += num
#
# print(count)
