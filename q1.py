

def swap(x, y):
    """
    Task 1
    - Create a function that would swap the value of x and y using only x and y as variables.
    - x and y must be numeric.
    - Return -1 if x and y is not numeric, and
    - print the swapped values if both x and y are numeric.
    """

    # Check if both x and y are numeric
    if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
        return -1

    # Swap x and y using only x and y
    x, y = y, x

    # Print the swapped values
    print(x, y)


# Task 2
# Invoke the function "swap" using the following scenarios:

print(swap("Apple", 10))  # Expected output: -1
swap(9, 17)               # Expected output: 17 9





