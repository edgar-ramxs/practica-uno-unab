# Fibonacci Numbers

# DOCS
# http://algorithmics.lsi.upc.edu/docs/Dasgupta-Papadimitriou-Vazirani.pdf
# pag 12 - pag 14

from argparse import ArgumentParser

parser = ArgumentParser(description="name of the input file")
parser.add_argument(
    "file_name", type=str, help="name of document with the example input"
)
args = parser.parse_args()
input = None

with open(f"./inputs/{args.file_name}", "r") as file:
    for line in file:
        input = [element.rstrip() for element in line.split(" ")][0]
        input = int(input)


# fib2 | dynamic programming
def fibonacci2(n: int):
    f = [0, 1]
    if n <= 1:
        return n
    for _ in range(n + 1):
        f.append(f[-1] + f[-2])
    return f[n]


output = fibonacci2(input)

with open(f"./outputs/output_{args.file_name}", "w") as output_file:
    output_file.write(str(output))

# Explanation in Rosalind
#
# def sqrt(n):
#     return n**0.5
# def Fibo(n):
#     return int(((1 + sqrt(5)) ** n - (1 - sqrt(5)) ** n) / (2**n * sqrt(5)))
#
# output = Fibo(input)
