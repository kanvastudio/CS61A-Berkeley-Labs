def cascade(n, x=1):
    print(x)
    if x < n:
        cascade(n, (x) * 10 + (x % 10 + 1))
        print(x)
        
cascade(123456789)