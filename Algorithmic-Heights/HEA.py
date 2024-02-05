# Building a Heap

# INFO
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
    # print(f"nodos -> {N}")
    # print(f"array -> {A}")



# def building_a_heap(A: list = A):

#     def heapify(heap, i):
#         """Given a heap and recently added element at heap[i], perform up-heap
#         operation to conserve the heap property"""
#         if i == 0:
#             return
#         parent = (i - 1) // 2
#         child = i
#         if heap[parent] > heap[child]:
#             return
#         else:
#             heap[parent], heap[child] = heap[child], heap[parent]
#             heapify(heap, parent)

#     heap = []
#     # build heap here
#     for i in range(len(A)):
#         # add element to the bottom level of the heap.
#         heap.append(A[i])
#         # heapify
#         heapify(heap, i)
#     # print heap
#     print(" ".join(map(str, heap)))


# def build_max_heap(arr: list = A):
#     n = len(arr)
#     # Perform "bubble up" for each element from the end to the beginning
#     for i in range(n - 1, 0, -1):
#         parent_index = (i - 1) // 2
#         current_index = i
#         # Bubble up until the max heap property is satisfied
#         while parent_index >= 0 and arr[parent_index] < arr[current_index]:
#             arr[parent_index], arr[current_index] = arr[current_index], arr[parent_index]
#             current_index = parent_index
#             parent_index = (current_index - 1) // 2
#     print(arr)


# def buildHeap(arr: list = A, N: int = N):

#     def heapify(arr, N, i):
#         largest = i     # Initialize largest as root
#         l = 2 * i + 1   # left = 2*i + 1
#         r = 2 * i + 2   # right = 2*i + 2

#         # If left child is larger than root
#         if l < N and arr[l] > arr[largest]:
#             largest = l

#         # If right child is larger than largest so far
#         if r < N and arr[r] > arr[largest]:
#             largest = r

#         # If largest is not root
#         if largest != i:
#             arr[i], arr[largest] = arr[largest], arr[i]

#             # Recursively heapify the affected sub-tree
#             heapify(arr, N, largest)

#     # Index of last non-leaf node
#     startIdx = N // 2 - 1

#     # Perform reverse level order traversal
#     # from last non-leaf node and heapify
#     # each node
#     for i in range(startIdx, -1, -1):
#         heapify(arr, N, i)


# building_a_heap()
# 
# build_max_heap()
# buildHeap()


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

###########################################################

with open(f"./outputs/output_{args.file_name}", "w") as output_file:
    building_a_max_heap()
    output_file.write(" ".join(map(str, A)))
