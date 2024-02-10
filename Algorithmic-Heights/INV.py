# Counting Inversions
# https://rosalind.info/problems/inv/

from argparse import ArgumentParser

parser = ArgumentParser(description="name of the input file")
parser.add_argument(
    "-file", "--file_name", type=str, help="name of document with the example input"
)
args = parser.parse_args()

with open(f"./inputs/{args.file_name}", "r") as file:
    N = int(file.readline().strip())
    A = list(map(int, file.readline().strip().split()))


def counting_inversions1(array: list = A):

    def merge(left, right):
        result = []
        inversions = 0
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
                inversions += len(left) - i
        result.extend(left[i:])
        result.extend(right[j:])
        return result, inversions

    if len(array) <= 1:
        return array, 0

    mid = len(array) // 2
    left, left_inv = counting_inversions1(array[:mid])
    right, right_inv = counting_inversions1(array[mid:])
    merged, inversions = merge(left, right)
    return merged, inversions + left_inv + right_inv


def counting_inversions2(A):

    def merge(left, right):
        merged = []
        inversions = 0
        i, j = 0, 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1
                inversions += len(left) - i
        merged += left[i:]
        merged += right[j:]
        return merged, inversions

    def merge_sort(A):
        if len(A) <= 1:
            return A, 0
        
        mid = len(A) // 2
        left, left_inversions = merge_sort(A[:mid])
        right, right_inversions = merge_sort(A[mid:])
        merged, merge_inversions = merge(left, right)
        return merged, left_inversions + right_inversions + merge_inversions

    _, inversions = merge_sort(A)
    return inversions


OUTPUT = str(counting_inversions1(A)[1])
# OUTPUT = str(counting_inversions2(A))


with open(f"./outputs/output_{args.file_name}", "w") as output_file:
    output_file.write(OUTPUT)
