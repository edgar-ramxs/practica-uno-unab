# 3SUM
# https://rosalind.info/problems/3sum/

from argparse import ArgumentParser

parser = ArgumentParser(description="name of the input file")
parser.add_argument(
    "-file", "--file_name", type=str, help="name of document with the example input"
)
args = parser.parse_args()

with open(f"./inputs/{args.file_name}", "r") as file:
    K, N = list(map(int, file.readline().split()))
    MATRIX = [list(map(int, line.split())) for line in file.readlines()]


def three_indices(arrays: list = MATRIX, k: int = K, n: int = N):
    output = ""

    for array in arrays:
        numbers = {}
        found = False

        for index in range(0, n):
            numbers[array[index]] = index

        for a in range(0, n):
            if found == True:
                break
            else:
                first = array[a]

            for b in range(a + 1, n):
                second = array[b]
                if ((-1) * (first + second)) in numbers:
                    c = numbers[(-1) * (first + second)]
                    output += f"{a+1} {b+1} {c+1}\n"
                    found = True
                    break

        if found == False:
            output += f"{-1}\n"

    return output


output = three_indices()


with open(f"./outputs/output_{args.file_name}", "w") as output_file:
    output_file.write(output)
