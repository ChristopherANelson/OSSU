# Simple is_even function def
def is_even (i):
    """
    Input: i, a positive int
    Returns True if i is even, otherwise False
    """
    remainder = i % 2
    return remainder == 0

print("All the numbers between 0 and 20: even or not")
for i in range(21):
    if is_even(i):
        print(i, "even")
    else:
        print(i, "odd")

