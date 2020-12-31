# Method to merge sort in Python
from typing import List, Set, Dict, Tuple, Optional

# Simple Appr0ach
def mergeSort(array1: List[int], array2: List[int]) -> List[int]:
    array1.extend(array2)
    return sorted(array1)

# Manual Approach
def mergeSortManual(array1: List[int], array2: List[int]) -> List[int]:

    merged_array = []
    a1_i = 0
    a2_i = 0

    # Check if either array is empty
    if not array1 or not array2:
        return array1 + array2

    array1_value = array1[0]
    array2_value = array2[0]

    while a1_i < len(array1) and a2_i < len(array2):
        if array1[a1_i] <= array2[a2_i]:
            merged_array.append(array1[a1_i])
            a1_i += 1
        else:
            merged_array.append(array2[a2_i])
            a2_i += 1

    return merged_array+array1[a1_i:]+array2[a2_i:]

print(mergeSort([0,3,4,31], [4,6,30]))
print(mergeSortManual([0,3,4,31], [4,6,30]))
print(mergeSortManual([], [4,6,30]))
print(mergeSortManual([2], [4,6,30]))