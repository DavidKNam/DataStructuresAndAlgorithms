# Implementation of Bubble Sort in Python

def bubbleSort(list):

    if not list:
        return
    else:
        if len(list) == 1:
            return list
        else:
            for i in range(len(list)):
                for j in range(len(list) -1):
                    if list[j] > list[j+1]:
                        list[j], list[j+1] = list[j+1], list[j]

    return list


numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0];
print(bubbleSort(numbers))