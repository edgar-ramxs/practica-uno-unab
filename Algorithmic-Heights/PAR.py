# 2-Way Partition
# https://rosalind.info/problems/par/

# INFO:
# -> https://programiz.com/dsa/quick-sort
# -> https://www.geeksforgeeks.org/python-program-for-quicksort/
# -> https://favtutor.com/blogs/quicksort-python


from argparse import ArgumentParser

parser = ArgumentParser(description="name of the input file")
parser.add_argument(
    "-file", "--file_name", type=str, help="name of document with the example input"
)
args = parser.parse_args()

with open(f"./inputs/{args.file_name}", "r") as file:
    N = int(file.readline().strip())
    A = list(map(int, file.readline().split()))


def partition(array):
    new_array, left_array, right_array = [], [], []
    new_array.append(array[0])
    for i in range(1, len(array)):
        if array[i] <= array[0]:
            left_array.append(array[i])
        else:
            right_array.append(array[i])
    new_array = left_array + new_array + right_array
    return new_array


# Ejemplo de uso:

B = partition(A)
print(B)


# def partition(array, low, high):
# 	# choose the rightmost element as pivot
# 	pivot = array[high]
# 	# pointer for greater element
# 	i = low - 1
# 	# traverse through all elements
# 	# compare each element with pivot
# 	for j in range(low, high):
# 		if array[j] <= pivot:
# 			# If element smaller than pivot is found
# 			# swap it with the greater element pointed by i
# 			i = i + 1
# 			# Swapping element at i with element at j
# 			(array[i], array[j]) = (array[j], array[i])
# 	# Swap the pivot element with the greater element specified by i
# 	(array[i + 1], array[high]) = (array[high], array[i + 1])
# 	# Return the position from where partition is done
# 	return i + 1


# # function to perform quicksort
# def quickSort(array, low, high):
# 	if low < high:
# 		# Find pivot element such that
# 		# element smaller than pivot are on the left
# 		# element greater than pivot are on the right
# 		pi = partition(array, low, high)
# 		# Recursive call on the left of pivot
# 		quickSort(array, low, pi - 1)
# 		# Recursive call on the right of pivot
# 		quickSort(array, pi + 1, high)

# quickSort(A, 0, len(A)-1)
# print(A)
