def factorial(n):
    """Calculate the factorial of the given number"""

    if n > 1:
        return n * factorial(n-1)
    else:
        return 1


assert factorial(5) == 120
