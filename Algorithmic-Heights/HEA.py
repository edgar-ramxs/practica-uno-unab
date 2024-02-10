# Building a Heap
# https://rosalind.info/problems/hea/

# INFO:
# https://www.youtube.com/watch?v=B7hVxCmfPtM
# https://www.geeksforgeeks.org/building-heap-from-array/
# https://medium.com/edureka/data-structures-algorithms-in-java-d27e915db1c5

from argparse import ArgumentParser

parser = ArgumentParser(description="name of the input file")
parser.add_argument(
    "-file", "--file_name", type=str, help="name of document with the example input"
)
args = parser.parse_args()

with open(f"./inputs/{args.file_name}", "r") as file:
    N = int(file.readline().strip())
    A = list(map(int, file.readline().split()))


def building_a_max_heap(a: list = A, n: int = N):
    for i in range(n - 1, 0, -1):
        parent = (i - 1) // 2
        if a[i] > a[parent]:
            a[parent], a[i] = a[i], a[parent]

            v = i
            while True:
                max_node = v
                if v * 2 + 1 < len(a) and a[v * 2 + 1] > a[max_node]:
                    max_node = v * 2 + 1
                if v * 2 + 2 < len(a) and a[v * 2 + 2] > a[max_node]:
                    max_node = v * 2 + 2
                if max_node == v:
                    break
                a[v], a[max_node] = a[max_node], a[v]
                v = max_node


with open(f"./outputs/output_{args.file_name}", "w") as output_file:
    building_a_max_heap()
    output_file.write(" ".join(map(str, A)))
