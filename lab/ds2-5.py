def sevens(n, k):
    """Return the (clockwise) position of who says n among k players.

    >>> sevens(2, 5)
    2
    >>> sevens(6, 5)
    1
    >>> sevens(7, 5)
    2
    >>> sevens(8, 5)
    1
    >>> sevens(9, 5)
    5
    >>> sevens(18, 5)
    2
    """
    def f(i, who, direction):
        if i == n:
            return who
        if i % 7 == 0 or '7' in str(i):
            direction *= -1
        i += 1
        who = (who + direction - 1) % k + 1
        if who == 0:
            if direction == 1:
                who = 1
            else:
                who = 5
        
        return f(i, who, direction)
    return f(1, 1, 1)
print(sevens(2, 5)) 
print(sevens(6, 5)) 
print(sevens(7, 5))
print(sevens(8, 5))
print(sevens(9, 5))
print(sevens(18, 5))  

    