1	def average(x, y):
2	    return (x + y)/2
3	
4	def improve(update, close, guess=1):
5	    while not close(guess):
6	        guess = update(guess)
7	    return guess
8	
9	def approx_eq(x, y, tolerance=1e-3):
10	    return abs(x - y) < tolerance
11	
12	def sqrt(a):
13	    def sqrt_update(x):
14	        return average(x, a/x)
15	    def sqrt_close(x):
16	        return approx_eq(x * x, a)
17	    return improve(sqrt_update, sqrt_close)
18	
19	result = sqrt(256)