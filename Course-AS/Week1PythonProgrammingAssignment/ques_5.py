def sum_of_divisors(number):
    """
    Write a Python Program that finds the sum of the divisors, and make sure
    that the divisor should be proper.

    Args:
        number (int): Number whose sum of divisors is to be found.

    Returns:
        int: Sum of divisors.
    """
    sum=0
    for x in range(1, int(number/2+1)):
        if number%x==0:
            sum=sum+x

    return sum

n=int(input("Enter a number: "))
print(sum_of_divisors(n))
