def skip_factorial(n):
    """
    The function `skip_factorial` calculates the product of positive integers skipping every other
    number starting from `n`.

    """
    """Return the product of positive integers n * (n - 2) * (n - 4) * ...
    >>> skip_factorial(5) # 5 * 3 * 1
    15
    >>> skip_factorial(8) # 8 * 6 * 4 * 2
    384
"""
    if 0 <= n <= 1:
        return 1
    else:
        return skip_factorial(n - 2) * n
    
print(skip_factorial(15))