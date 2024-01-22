# 2SUM

from argparse import ArgumentParser

parser = ArgumentParser(description="name of the input file")
parser.add_argument(
    "-file", "--file_name", type=str, help="name of document with the example input"
)
args = parser.parse_args()

with open(f"./inputs/{args.file_name}", "r") as file:
    INPUT = [list(map(int, line.split())) for line in file]
    K, N = INPUT.pop(0)


def two_sum2(matrix: list = INPUT) -> str:
    def find_pairs(array: list) -> str:
        result = {}
        for index, value in enumerate(array):
            opposite = -value
            if opposite in result:
                return f"{result[opposite] + 1} {index + 1}"
            else:
                result[value] = index
        return "-1"

    output = ""
    for array in matrix:
        output += f"{find_pairs(array)}\n"
    return output


with open(f"./outputs/output_{args.file_name}", "w") as output_file:
    output_file.write(str(two_sum2()))
