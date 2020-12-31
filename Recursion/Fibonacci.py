# Given a number N return the index value of the Fibonacci sequence, where the sequence is:

# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144 ...
# the pattern of the sequence is that each value is the sum of the 2 previous values, that means that for N=5 -> 2+3

def fibonacciIterative(n):
    previous_value = 0
    current_value = 1
    for index in range(n - 1):
        total_value = previous_value + current_value
        previous_value = current_value
        current_value = total_value

    return total_value

def fibonacciRecursive(n):
    return fibonacciRecursive(n - 1) + fibonacciRecursive(n - 2) if n > 1 else n

print(fibonacciIterative(5))
print(fibonacciRecursive(5))
print(fibonacciIterative(8))
print(fibonacciRecursive(8))