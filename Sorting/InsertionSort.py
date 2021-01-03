# Implementation of Insertion Sort in Python

def insertionSort(list):
    if not list:
        return

    if len(list) == 1:
        return list
    else:
        end = list[0]
        for i in range(1, len(list)):
            if list[i] < end:
                tmp = list.pop(i)
                for j in range(0, i):
                    if tmp < list[j]:
                        list.insert(j, tmp)
                        break;
                end = list[i]
    return list

numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0];
print(insertionSort(numbers))