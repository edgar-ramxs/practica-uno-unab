# 3SUM

from argparse import ArgumentParser

parser = ArgumentParser(description="name of the input file")
parser.add_argument(
    "-file", "--file_name", type=str, help="name of document with the example input"
)
args = parser.parse_args()

with open(f"./inputs/{args.file_name}", "r") as file:
    K, N = list(map(int, file.readline().split()))
    MATRIX = [list(map(int, line.split())) for line in file.readlines()]


############################################

# def two_sum(a, target2=0):
#     tmp_dict = {}
#     for i in range(len(a)):
#         if a[i] in tmp_dict:
#             return (tmp_dict[a[i]]+1, i+1)
#         else:
#             tmp_dict[target2-a[i]] = i
#     return -1

# def three_sum(a, target3=0):
#     for i in range(len(a)):
#         res = two_sum(a[i+1:], target2=target3-a[i])
#         if res != -1:
#             print(i+1, i+1+res[0], i+1+res[1])
#             return (i+1, i+1+res[0], i+1+res[1])
#     print(-1)
#     return -1

# for array in MATRIX:
#     r = three_sum(array)


##########################################


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
