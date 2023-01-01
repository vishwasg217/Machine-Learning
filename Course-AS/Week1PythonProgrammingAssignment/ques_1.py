def program_to_print_multiplication_table(number):
    """
    Write a Python Program that can print the list of multiplication table of a
    number.

    Args:
        number (int): Number whose multiplication table is to be printed.

    Returns:
        list: List of multiplication table of the number.
    """
    table=[]

    for x in range(1, 11):
        table.append(x*number)

    return table


number = int(input("Enter a number: "))
table = program_to_print_multiplication_table(number)

print(table)


