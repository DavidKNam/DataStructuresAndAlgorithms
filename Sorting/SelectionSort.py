# Implementation of Selection Sort in Python

def selectionSort(list):
    if not list:
        return

    if len(list) == 0:
        return list
    else:
        for i in range(len(list)):
            min_value = list[i]
            min_index = i
            for j in range(i+1, len(list)):
                if list[j] < min_value:
                    min_value = list[j]
                    min_index = j
            list[i], list[min_index] = min_value, list[i]

        return list

numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0];
print(selectionSort(numbers))