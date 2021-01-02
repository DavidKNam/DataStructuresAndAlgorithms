# Reversing String Using Recursion

def reverseString(inputString):
    return inputString[-1] + reverseString(inputString[:len(inputString)-1]) if len(inputString) > 1 else inputString

print(reverseString("HelloWorld"))
print(reverseString("H"))
print(reverseString(""))