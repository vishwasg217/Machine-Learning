def filter_odd_numbers(numbers):
    """
    Write a program which can filter odd numbers in a list by using filter
    function.

    Args:
        numbers (list): List of numbers.

    Returns:
        list: List of odd numbers.
    """
    result = filter(lambda x: x % 2 != 0, numbers)
    return result

print("Enter the numbers: ")
list1 = list(map(int, input().split(" ")))
ans = filter_odd_numbers(list1)
print("Odd numbers: ")
for x in ans:
    print(x)



