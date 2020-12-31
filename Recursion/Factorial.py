# Write two functions that finds the factorial of any number.
# One should use recursive, the other should just use a for loop

def findFactorialRecursive(number):
    return number * findFactorialRecursive(number - 1) if number > 2 else 2

def findFactorialIterative(number):

    for factorial in range(2, number):
        number = number * factorial

    return number

print(findFactorialRecursive(3))
print(findFactorialIterative(3))
print(findFactorialRecursive(5))
print(findFactorialIterative(5))