# Dictionaries
# https://rosalind.info/problems/ini6/

from argparse import ArgumentParser

parser = ArgumentParser(description="name of the input file")
parser.add_argument(
    "-file", "--file_name", type=str, help="name of document with the example input"
)
args = parser.parse_args()

with open(f"./inputs/{args.file_name}", "r") as file:
    WORDS = file.readline().strip().split()
    OUTPUT = ""
    DICTIONARY = dict()

for word in WORDS:
    if not word in DICTIONARY:
        DICTIONARY[word] = 1
    else:
        DICTIONARY[word] += 1

for word, appearances in DICTIONARY.items():
    OUTPUT += f"{word} {appearances}\n"

with open(f"./outputs/output_{args.file_name}", "w") as output_file:
    output_file.write(OUTPUT)
