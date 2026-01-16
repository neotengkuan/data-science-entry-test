


def check_divisibility(num, divisor):
    """
    Task 1
    - Create a function to check if the number (num) is divisible by another number (divisor).
    - Both num and divisor must be numeric.
    - Return True if num is divisible by divisor, False otherwise.
    """

    # Check if both inputs are numeric
    if not isinstance(num, (int, float)) or not isinstance(divisor, (int, float)):
        return False

    # Avoid division by zero
    if divisor == 0:
        return False

    # Check divisibility
    return num % divisor == 0


# Task 2
# Invoke the function using the given scenarios

print(check_divisibility(10, 2))  # Expected: True
print(check_divisibility(7, 3))   # Expected: False


