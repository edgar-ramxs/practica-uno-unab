# Introduction to the Bioinformatics Armory

from argparse import ArgumentParser

parser = ArgumentParser(description="name of the input file")
parser.add_argument(
    "file_name", type=str, help="name of document with the example input"
)
args = parser.parse_args()
output = ""

with open(f"./inputs/{args.file_name}", "r") as file:
    DNA = file.readline().strip().split()[0]

dna_string = sorted(set(DNA))
for nucleotides in dna_string:
    output += f"{DNA.count(nucleotides)} "

del dna_string
del DNA

with open(f"./outputs/output_{args.file_name}", "w") as output_file:
    output_file.write(str(output))
