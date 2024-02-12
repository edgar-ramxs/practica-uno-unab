# Partial Sort
# https://rosalind.info/problems/ps/

# INFO:
# https://dev.to/dottt/sorting-algorithm-with-python-code-ilo
# https://en.wikipedia.org/wiki/Partial_sorting


from argparse import ArgumentParser

parser = ArgumentParser(description="name of the input file")
parser.add_argument(
    "-file", "--file_name", type=str, help="name of document with the example input"
)
args = parser.parse_args()

with open(f"./inputs/{args.file_name}", "r") as file:
    N = int(file.readline().strip())
    A = list(map(int, file.readline().split()))
    K = int(file.readline().strip())


# Example
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]
        merge_sort(left_half)
        merge_sort(right_half)
        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

# B = A.copy()
# import time
# start_time = time.time()
merge_sort(A)
# print("--- %s seconds ---" % (time.time() - start_time))
# start_time = time.time()
# B.sort()
# print("--- %s seconds ---" % (time.time() - start_time))

OUTPUT = " ".join(map(str, A[:K]))

with open(f"./outputs/output_{args.file_name}", "w") as output_file:
    output_file.write(OUTPUT)
