SOURCE_FILE = __file__


def num_eights(num):
    """Returns the number of times 8 appears as a digit of num.

    >>> num_eights(3)
    0
    >>> num_eights(8)
    1
    >>> num_eights(88888888)
    8
    >>> num_eights(2638)
    1
    >>> num_eights(86380)
    2
    >>> num_eights(12345)
    0
    >>> num_eights(8782089)
    3
    >>> from construct_check import check
    >>> # ban all assignment statements
    >>> check(SOURCE_FILE, 'num_eights',
    ...       ['Assign', 'AnnAssign', 'AugAssign', 'NamedExpr', 'For', 'While'])
    True
    """
    if num == 0:
        return 0
    elif num % 10 == 8:
        return 1 + num_eights(num // 10)
    else:
        return num_eights(num // 10)
    

def digit_distance(num):
    """Determines the digit distance of num.

    >>> digit_distance(3)
    0
    >>> digit_distance(777) # 0 + 0
    0
    >>> digit_distance(314) # 2 + 3
    5
    >>> digit_distance(31415926535) # 2 + 3 + 3 + 4 + ... + 2
    32
    >>> digit_distance(3464660003)  # 1 + 2 + 2 + 2 + ... + 3
    16
    >>> from construct_check import check
    >>> # ban all loops
    >>> check(SOURCE_FILE, 'digit_distance',
    ...       ['For', 'While'])
    True
    """
    if num < 10:
        return 0
    else:
        last, second_last = num % 10, (num // 10) % 10
        return abs(last - second_last) + digit_distance(num // 10)


def interleaved_sum(num, f_odd, f_even):
    """Compute the sum f_odd(1) + f_even(2) + f_odd(3) + ..., up
    to num.

    >>> identity = lambda x: x
    >>> square = lambda x: x * x
    >>> triple = lambda x: x * 3
    >>> interleaved_sum(5, identity, square) # 1   + 2*2 + 3   + 4*4 + 5
    29
    >>> interleaved_sum(5, square, identity) # 1*1 + 2   + 3*3 + 4   + 5*5
    41
    >>> interleaved_sum(4, triple, square)   # 1*3 + 2*2 + 3*3 + 4*4
    32
    >>> interleaved_sum(4, square, triple)   # 1*1 + 2*3 + 3*3 + 4*3
    28
    >>> from construct_check import check
    >>> check(SOURCE_FILE, 'interleaved_sum', ['While', 'For', 'Mod']) # ban loops and %
    True
    >>> check(SOURCE_FILE, 'interleaved_sum', ['BitAnd', 'BitOr', 'BitXor']) # ban bitwise operators, don't worry about these if you don't know what they are
    True
    """
    if num == 1:
        return f_odd(1)
    elif num / 2 == num // 2:
        return f_even(num) + interleaved_sum(num - 1, f_odd, f_even)
    else:
        return f_odd(num) + interleaved_sum(num - 1, f_odd, f_even)


def next_smaller_dollar(bill):
    """Returns the next smaller bill in order."""
    if bill > 50:
        return 50
    if bill > 20:
        return 20
    if bill > 10:
        return 10
    if bill > 5:
        return 5
    if bill > 1:
        return 1
    return None

def count_dollars(sum_needed):
    """Return the number of ways to make change.

    >>> count_dollars(15)  # 15 $1 bills, 10 $1 & 1 $5 bills, ... 1 $5 & 1 $10 bills
    6
    >>> count_dollars(10)  # 10 $1 bills, 5 $1 & 1 $5 bills, 2 $5 bills, 10 $1 bills
    4
    >>> count_dollars(20)  # 20 $1 bills, 15 $1 & $5 bills, ... 1 $20 bill
    10
    >>> count_dollars(45)  # How many ways to make change for 45 dollars?
    44
    >>> count_dollars(100) # How many ways to make change for 100 dollars?
    344
    >>> count_dollars(200) # How many ways to make change for 200 dollars?
    3274
    >>> from construct_check import check
    >>> # ban iteration
    >>> check(SOURCE_FILE, 'count_dollars', ['While', 'For'])
    True
    """
    def count_with_max(total, max_bill):
        if total == 0:
            return 1 # Found a valid way to make change
        if total < 0 or max_bill is None:
            return 0 # Went over the total or ran out of bills
        
        # Option 1: Use the max_bill at least once
        use_bill = count_with_max(total - max_bill, max_bill)
        
        # Option 2: Don't use this max_bill anymore, move to the next smaller one
        skip_bill = count_with_max(total, next_smaller_dollar(max_bill))
        
        return use_bill + skip_bill

    # Start with the highest possible bill for the given sum
    if sum_needed >= 100: start_bill = 100
    elif sum_needed >= 50: start_bill = 50
    elif sum_needed >= 20: start_bill = 20
    elif sum_needed >= 10: start_bill = 10
    elif sum_needed >= 5:  start_bill = 5
    else: start_bill = 1

    return count_with_max(sum_needed, start_bill)



def next_larger_dollar(bill):
    """Returns the next larger bill in order."""
    if bill == 1:
        return 5
    elif bill == 5:
        return 10
    elif bill == 10:
        return 20
    elif bill == 20:
        return 50
    elif bill == 50:
        return 100

def count_dollars_upward(sum_needed):
    """Return the number of ways to make change using bills.

    >>> count_dollars_upward(15)  # 15 $1 bills, 10 $1 & 1 $5 bills, ... 1 $5 & 1 $10 bills
    6
    >>> count_dollars_upward(10)  # 10 $1 bills, 5 $1 & 1 $5 bills, 2 $5 bills, 10 $1 bills
    4
    >>> count_dollars_upward(20)  # 20 $1 bills, 15 $1 & $5 bills, ... 1 $20 bill
    10
    >>> count_dollars_upward(45)  # How many ways to make change for 45 dollars?
    44
    >>> count_dollars_upward(100) # How many ways to make change for 100 dollars?
    344
    >>> count_dollars_upward(200) # How many ways to make change for 200 dollars?
    3274
    >>> from construct_check import check
    >>> # ban iteration
    >>> check(SOURCE_FILE, 'count_dollars_upward', ['While', 'For'])
    True
    """
    def count_helper(amount, smallest_bill):
        # Base Case 1: If amount is 0, we found a valid combination
        if amount == 0:
            return 1
        # Base Case 2: If amount is negative or we've run out of bill types
        if amount < 0 or smallest_bill is None:
            return 0
        
        # The transition to the next bill type using a lambda
        get_next = lambda b: next_larger_dollar(b)
        
        # Recursive Step:
        # 1. Use the current smallest bill (subtract from amount, keep bill the same)
        # 2. Skip the current smallest bill (amount stays same, move to next larger)
        return count_helper(amount - smallest_bill, smallest_bill) + \
               count_helper(amount, get_next(smallest_bill))

    # Start the recursion with the smallest possible bill (1)
    return count_helper(sum_needed, 1)


def print_move(origin, destination):
    """Print instructions to move a disk."""
    print("Move the top disk from rod", origin, "to rod", destination)

def move_stack(num, start, end):
    """Print the moves required to move num disks on the start pole to the end
    pole without violating the rules of Towers of Hanoi.

    num -- number of disks
    start -- a pole position, either 1, 2, or 3
    end -- a pole position, either 1, 2, or 3

    There are exactly three poles, and start and end must be different. Assume
    that the start pole has at least num disks of increasing size, and the end
    pole is either empty or has a top disk larger than the top num start disks.

    >>> move_stack(1, 1, 3)
    Move the top disk from rod 1 to rod 3
    >>> move_stack(2, 1, 3)
    Move the top disk from rod 1 to rod 2
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 2 to rod 3
    >>> move_stack(3, 1, 3)
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 1 to rod 2
    Move the top disk from rod 3 to rod 2
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 2 to rod 1
    Move the top disk from rod 2 to rod 3
    Move the top disk from rod 1 to rod 3
    """
    assert 1 <= start <= 3 and 1 <= end <= 3 and start != end, "Bad start/end"
    # Base Case: If there are no disks to move, do nothing.
    if num == 0:
        return
    
    # Identify the "spare" rod (the one that is not start or end)
    spare = 6 - start - end
    
    # Step 1: Move the top (num - 1) disks from start to spare
    move_stack(num - 1, start, spare)
    
    # Step 2: Move the largest (bottom) disk from start to end
    print_move(start, end)
    
    # Step 3: Move the (num - 1) disks from spare to end
    move_stack(num - 1, spare, end)


from operator import sub, mul

def make_anonymous_factorial():
    """Return the value of an expression that computes factorial.

    >>> make_anonymous_factorial()(5)
    120
    >>> from construct_check import check
    >>> # ban any assignments or recursion
    >>> check(SOURCE_FILE, 'make_anonymous_factorial',
    ...     ['Assign', 'AnnAssign', 'AugAssign', 'NamedExpr', 'FunctionDef', 'Recursion'])
    True
    """
    return (lambda f: (lambda x: x(x))(lambda x: f(lambda y: x(x)(y))))(lambda f: lambda n: 1 if n == 0 else mul(n, f(sub(n, 1))))