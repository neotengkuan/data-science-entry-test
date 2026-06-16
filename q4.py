




def string_reverse(s):
    """
    Task 1
    - Create a function that reverses a given string (s).
    - s must be a string.
    - Return the reversed string.
    """

    if not isinstance(s, str):
        return -1

    return s[::-1]


Explanation:

s[::-1] is Python's shorthand for reversing a string.
isinstance(s, str) checks that the input is actually a string.
Returns -1 if the input is not a string.






# Task 2
# Invoke the function "string_reverse" using the following scenarios:
# - "Hello World"
# - "Python"

print(string_reverse("Hello World"))

print(string_reverse("Python"))



dlroW olleH
nohtyP
