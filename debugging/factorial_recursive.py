#!/usr/bin/python3
import sys


def factorial(n):
    """
    Function Description:
    Computes the factorial of a given non-negative integer using recursion.

    Parameters:
    n (int): The number for which the factorial is calculated.

    Returns:
    int: The factorial of the input number n.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


f = factorial(int(sys.argv[1]))
print(f)
