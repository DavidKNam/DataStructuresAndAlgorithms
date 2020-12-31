# Write two functions that finds the factorial of any number.
# One should use recursive, the other should just use a for loop

def findFactorialRecursive(number):
    return number * findFactorialRecursive(number - 1) if number > 1 else 1

def findFactorialIterative(number):
    result = 1
    for factorial in range(1, number + 1):
        result = result * factorial

    return result

print(findFactorialRecursive(3))
print(findFactorialIterative(3))
print(findFactorialRecursive(5))
print(findFactorialIterative(5))
print(findFactorialRecursive(0))
print(findFactorialIterative(0))
print(findFactorialRecursive(1))
print(findFactorialIterative(1))
