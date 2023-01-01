def sum_of_even_numbers(number):
    """
    Write a Python Program that prints out the sum of all even numbers from 1 to
    N.

    Args:
        number (int): Number till which sum of even numbers is to be found.

    Returns:
        int: Sum of even numbers.
    """
    sum = 0
    for x in range(0, number+1, 2):
        sum+=x

    return sum

n=int(input("Enter a number: "))
print(sum_of_even_numbers(n))
