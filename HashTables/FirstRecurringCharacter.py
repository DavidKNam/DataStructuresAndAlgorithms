# Method to find first recurring character

def firstRecurring(array) -> int:

    # Could use hashset instead
    recurring = set()

    for value in array:
        if value in recurring:
            return value
        else:
            recurring.add(value)

    return None

def firstRecurring2(array) -> int:

    recurring = {}

    for value in array:
        if value in recurring:
            return value
        else:
            recurring[value] = 0

    return None

print(firstRecurring([1,2,2,4,5,5]))
print(firstRecurring2([1,2,4,5,5,6]))
