# Given a number N return the index value of the Fibonacci sequence using Memoization

# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144 ...
# the pattern of the sequence is that each value is the sum of the 2 previous values, that means that for N=5 -> 2+3

import functools

@functools.lru_cache()
def fibonacciRecursive(n):
    return fibonacciRecursive(n - 1) + fibonacciRecursive(n - 2) if n > 1 else n

# Global Variable
cache = {}
def fibonacciRecursive2(n):
    if n in cache:
        return cache[n]
    else:
        if n < 2:
            return n
        else:
            cache[n] = fibonacciRecursive2(n - 1) + fibonacciRecursive2(n - 2)
            return cache[n]

# Decorator
def fibonacciRecursive3():
    cache2 = {}
    def memoized_fib(n):
        if n in cache2:
            return cache2[n]
        else:
            if n < 2:
                return n
            else:
                cache2[n] = fibonacciRecursive2(n - 1) + fibonacciRecursive2(n - 2)
                return cache2[n]

    return memoized_fib

# Bottom Up Approach
def fibonacci_Bottomup(n):
    answers = [0, 1]

    if n < 2:
        return n
    else:
        i = 2
        while i <= n:
            answers.append(answers[i-1] + answers[i-2])
            i += 1
    return answers.pop()


print(fibonacciRecursive(5))
print(fibonacciRecursive(8))
print(fibonacciRecursive(50))
print(fibonacciRecursive(100))
print(fibonacciRecursive.cache_info())

print(fibonacciRecursive2(5))
print(fibonacciRecursive2(8))
print(fibonacciRecursive2(50))
print(fibonacciRecursive2(100))

mem_fib = fibonacciRecursive3()
print(mem_fib(5))
print(mem_fib(8))
print(mem_fib(50))
print(mem_fib(100))

print(fibonacci_Bottomup(5))
print(fibonacci_Bottomup(8))
print(fibonacci_Bottomup(50))
print(fibonacci_Bottomup(100))
