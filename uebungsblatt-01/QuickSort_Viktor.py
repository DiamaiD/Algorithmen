"""
Design sketch for QuickSort Algorithm.

"""
import random
import time

def quicksort(array, if_randomized=True):
    """
    Sort array in ascending order.
    Wrapper for the sorting method.

    Args:
        int[] array:    integer array
        bool if_randomized:    method how to pick pivot. True if randomized.
    """
    print(array)
    quicksort_recursive(array, 0, len(array)-1, if_randomized)
    print(array)


def quicksort_recursive(array, left, right, if_randomized):
    """
    Method that recursively divides array on parts and calls the
    rearrangement procedure on each part.

    Args:
        int[] array:    integer array that has to be sorted
        int left:    left index from which the rearrangement starts.
        int right:    right index till which the rearrangement goes.
        bool if_randomized:    method how to pick pivot. True if randomized.
    """
    if left < right:
        pivot = quicksort_divide(array, left, right, if_randomized)
        quicksort_recursive(array, left, pivot-1, if_randomized)
        quicksort_recursive(array, pivot+1, right, if_randomized)



def quicksort_divide(array, left, right, if_randomized):
    """
    Method that executes the divide step of the algorithm. Method chooses
    pivot element and  performs rearrangement of the elements inside of
    the array in such a way, that elements that are smaller than pivot are
    placed to the left of it, and elements that are larger than pivot are
    placed the the right of pivot.

    Args:
        int[] array:    integer array that has to be rearranged.
        int left:    left index from which the rearrangement starts.
        int right:    right index till which the rearrangement goes.
        bool if_randomized:    method how to pick pivot. True if randomized.
    Returns:
        int:    index where the pivot after the split is.
    """

    if if_randomized == True:
        pivotindex = array.index(random.choice(array[left:right+1]))
        pivot = array[pivotindex]
    else:
        pivot = array[right]
        pivotindex = right

    for i in range(left, right):
        if array[i] < pivot:
            array[left], array[i] = array[i], array[left]
            left += 1

    array[left], array[pivotindex] = array[pivotindex], array[left]

    return left

arraytest = [20,4,8,2,6,3,10,7,234,5464,64577,1,1,454,4]

print("\nnot random")
quicksort(arraytest, False)

print("\nrandom")
quicksort(arraytest)
