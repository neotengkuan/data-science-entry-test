


def swap(x, y):
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
        return -1

    x, y = y, x
    print("x =", x)
    print("y =", y)


print(swap("Apple", 10))
swap(9, 17)




-1
x = 17
y = 9



