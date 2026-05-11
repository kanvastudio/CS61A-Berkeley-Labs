def is_prime(n, divisor=2):
    """Returns True if n is a prime number and False otherwise.
    >>> is_prime(2)
    True
    >>> is_prime(16)
    False
    >>> is_prime(521)
    True
    """

    if divisor * divisor > n:
        return True
    if n % divisor == 0:
        return False
    return is_prime(n, divisor + 1)

print(is_prime(2))
print (is_prime(16))
print(is_prime(521))