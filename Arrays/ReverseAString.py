# Method to reverse string in python

# Simple Approach
def reverse(string):
    return string[::-1]

# Manual Approach
def reverseManual(string):
    # Check if it is string
    if isinstance(string, str):
        string_array = list(string)
        reversed_string = ""
        j = len(string) - 1
        while j >= 0:
            reversed_string += string_array[j]
            j -= 1
        return reversed_string
    else:
        return "Given variable is not a String"

def reverseManual2(string: str) -> str:
    string_array = list(string)
    i = 0
    j = len(string) - 1
    while i != j and i < j:
        tmp = string_array[i]
        string_array[i] = string_array[j]
        string_array[j] = tmp
        i += 1
        j -= 1
    return "".join(string_array)

print("Hello World")
print(reverse("Hello World"))
print(reverseManual("Hello World"))
print(reverseManual(5))
print(reverseManual2("Hello World"))
