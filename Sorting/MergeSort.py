# Implementation of Merge Sort in Python

def mergeSort(list):
    if not list:
        return

    if len(list) == 1:
        return list
    else:
        middle = len(list) // 2
        left = list[:middle]
        right = list[middle:]

    return merge(mergeSort(left), mergeSort(right))

def merge(left, right):
    combined = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            combined.append(left[i])
            i += 1
        else:
            combined.append(right[j])
            j += 1
    return combined + left[i:] + right[j:]

numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0];
print(mergeSort(numbers))