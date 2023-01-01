import math


def decimal_to_binary(num):
    """
    Write a Python Program to convert decimal to binary number.

    Args:
        num (int): Decimal number to be converted to binary.

    Returns:
        int: Binary number.
    """

    ans=0
    i=0
    while num>0:
        ans=ans+(num%2)*math.pow(10, i)
        num=num//2
        i+=1

    return ans


num=int(input("Enter a decimal number: "))
print("Binary format: ",int(decimal_to_binary(num)))

        

