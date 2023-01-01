import math


def cube_of_numbers(numbers):
    """
    Write a program which can map() to make a list whose elements are cube of
    elements in a given list.

    Args:
        numbers (list): List of numbers.

    Returns:
        list: List of cubes of the numbers.
    """
    result = map(lambda x: math.pow(x, 3), numbers)
    return result

print("Enter the numbers: ")
list1 = list(map(int, input().split(" ")))
ans = cube_of_numbers(list1)
print("Odd numbers: ")
for x in ans:
    print(x)
