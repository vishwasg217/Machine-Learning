import math


def print_perfect_numbers_in_range(start, end):
    """
    Write a Python Program that prints out all the perfect numbers in a given
    range.

    Args:
        start (int): Start of the range.
        end (int): End of the range.

    Returns:
        list: List of perfect numbers in the range.
    """
    ans=[]
    for n in range(start, end+1):
        sum = 0
        for i in range(1, n):
            if n%i == 0:
                sum += i
        #print(n, sum)

        if n == sum:
            ans.append(n)
    
    return ans

ans=print_perfect_numbers_in_range(2, 10000)
print(ans)
