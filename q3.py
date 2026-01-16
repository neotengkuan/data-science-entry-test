



def update_dictionary(dct, key, value):
    """
    Task 1
    - Create a function that updates a dictionary (dct) with a new key-value pair.
    - If the key already exists in dct, print the original value, then update its value.
    - Return the updated dictionary.
    """

    # If key exists, print original value
    if key in dct:
        print(dct[key])

    # Update or add the key-value pair
    dct[key] = value

    return dct


# Task 2
# Invoke the function using the given scenarios

print(update_dictionary({}, "name", "Alice"))
print(update_dictionary({"age": 25}, "age", 26))

