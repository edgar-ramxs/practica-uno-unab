# 3-Way Partition
# https://rosalind.info/problems/par3/


from argparse import ArgumentParser

parser = ArgumentParser(description="name of the input file")
parser.add_argument(
    "-file", "--file_name", type=str, help="name of document with the example input"
)
args = parser.parse_args()


with open(f"./inputs/{args.file_name}", "r") as file:
    N = int(file.readline().strip())
    A = list(map(int, file.readline().split()))


def three_way_partition(array: list = A, n: int = N) -> None:
    pivot = array[0]
    leftLess, left, right, rightGreater = 0, 0, n - 1, n - 1

    while left <= right:

        while left <= right and array[left] <= pivot:
            if array[left] < pivot:
                array[leftLess], array[left] = array[left], array[leftLess]
                leftLess += 1
            left += 1
        array[left], array[right] = array[right], array[left]

        while left <= right and array[right] >= pivot:
            if array[right] > pivot:
                array[right], array[rightGreater] = array[rightGreater], array[right]
                rightGreater -= 1
            right -= 1
        array[left], array[right] = array[right], array[left]


three_way_partition()


OUTPUT = " ".join(map(str, A))
with open(f"./outputs/output_{args.file_name}", "w") as output_file:
    output_file.write(OUTPUT)
