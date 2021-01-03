# Implementation of Quick Sort in Python

def quickSort(list, left, right):
    if left < right:
        pivot = right
        partitionindex = partition(list, pivot, left, right)

        quickSort(list, left, partitionindex - 1)
        quickSort(list, partitionindex + 1, right)
    return list

def partition(array, pivot, left, right):
    pivotvalue = array[pivot]
    partitionindex = left

    for i in range(left,right):
        if array[i] < pivotvalue:
            swap(array, i, partitionindex)
            partitionindex += 1

    swap(array, right, partitionindex)
    return partitionindex

def swap(array, firstindex, secondindex):
    temp = array[firstindex]
    array[firstindex] = array[secondindex]
    array[secondindex] = temp

numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0];
print(quickSort(numbers, 0, len(numbers)-1))