# Working with Files

from argparse import ArgumentParser

parser = ArgumentParser(description="name of the input file")
parser.add_argument(
    "file_name", type=str, help="name of document with the example input"
)
args = parser.parse_args()

output = ""

with open(f"./inputs/{args.file_name}", "r") as file:
    for num, line in enumerate(file):
        if (num + 1) % 2 == 0:
            output += line

with open(f"./outputs/output_{args.file_name}", "w") as output_file:
    output_file.write(output)
