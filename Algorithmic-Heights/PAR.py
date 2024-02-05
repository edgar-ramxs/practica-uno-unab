# 2-Way Partition

# INFO:
# QUICK SORT
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

def partition(a):
    pivot = a[0]
    left, right = 0, len(a) - 1
    while left != right:
        while right != left and a[right] > pivot:
            right -= 1
        a[left], a[right] = a[right], a[left]
        while left != right and a[left] <= pivot:
            left += 1
        a[left], a[right] = a[right], a[left]

def two_way_partition(a):
    '''Performs a 2-way partition on the array a.'''
    # Trivial with list comprehensions.
    return [x for x in a[1:] if x <= a[0]] + [a[0]] + [x for x in a[1:] if x > a[0]]

def partition2(array):
    new_array, left_array, right_array = [], [], []
    new_array.append(array[0])
    for i in range(1, len(array)):
        if array[i] <= array[0]:
            left_array.append(array[i])
        else:
            right_array.append(array[i])
    new_array = left_array + new_array + right_array
    return new_array

B = partition2(A)
print(B)

def quicksort(arr):
    if len(arr) < 2:
        return arr
    pivot = arr[0]
    left = [x for x in arr[1:] if x < pivot]
    right = [x for x in arr[1:] if x >= pivot]
    return quicksort(left) + [pivot] + quicksort(right)


def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        left = [x for x in arr[1:] if x < pivot]
        right = [x for x in arr[1:] if x >= pivot]
        return quicksort(left) + [pivot] + quicksort(right)
    

# Python program for implementation of Quicksort Sort
# This implementation utilizes pivot as the last element in the nums list
# It has a pointer to keep track of the elements smaller than the pivot
# At the very end of partition() function, the pointer is swapped with the pivot
# to come up with a "sorted" nums relative to the pivot
    
# Function to find the partition position
def partition(array, low, high):
	# choose the rightmost element as pivot
	pivot = array[high]
	# pointer for greater element
	i = low - 1
	# traverse through all elements
	# compare each element with pivot
	for j in range(low, high):
		if array[j] <= pivot:
			# If element smaller than pivot is found
			# swap it with the greater element pointed by i
			i = i + 1
			# Swapping element at i with element at j
			(array[i], array[j]) = (array[j], array[i])
	# Swap the pivot element with the greater element specified by i
	(array[i + 1], array[high]) = (array[high], array[i + 1])
	# Return the position from where partition is done
	return i + 1

# function to perform quicksort
def quickSort(array, low, high):
	if low < high:
		# Find pivot element such that
		# element smaller than pivot are on the left
		# element greater than pivot are on the right
		pi = partition(array, low, high)
		# Recursive call on the left of pivot
		quickSort(array, low, pi - 1)
		# Recursive call on the right of pivot
		quickSort(array, pi + 1, high)
