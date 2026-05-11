def hailstone(n, counter=1):
    """Print out the hailstone sequence starting at n, 
    and return the number of elements in the sequence.
    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    >>> b = hailstone(1)
    1
    >>> b
    1
    """
    if n == 1:
        print(n)
        return counter
    counter += 1
    print(n)
    if n % 2 == 0:
        return even(n, counter)
    else:
        return odd(n, counter)

def even(n, counter):
    return hailstone(n // 2, counter)

def odd(n, counter):
    return hailstone(3 * n + 1, counter)

print(hailstone(6))
    

