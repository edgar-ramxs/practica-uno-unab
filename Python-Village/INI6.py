# Dictionaries

from argparse import ArgumentParser

parser = ArgumentParser(description="name of the input file")
parser.add_argument(
    "file_name", type=str, help="name of document with the example input"
)
args = parser.parse_args()
dictionary = dict()
words = None
output = ""

with open(f"./inputs/{args.file_name}", "r") as file:
    for line in file:
        words = [word.rstrip() for word in line.split(" ")]

for word in words:
    if not word in dictionary:
        dictionary[word] = 1
    else:
        dictionary[word] += 1

for word, appearances in dictionary.items():
    output += f"{word} {appearances}\n"

with open(f"./outputs/output_{args.file_name}", "w") as output_file:
    output_file.write(output)
