#1.1
def wears_jacket(temp, raining):
    if temp<60 or raining == True:
        return True
    else:
        return False

#1.2
def handle_overflow(s1,s2):
    if s1>30 and s2>30:
        print("No space left in either section")
    elif s1>30 and s2<30:
        moved_amount = 30-s2
        print(f"Move to Section 2: {moved_amount}")
    elif s2>30 and s1<30:
        moved_amount = 30-s1
        print(f"Move to Section 1: {moved_amount}")
    else:
        print("No overflow")
#1.3
# def square(x):
#     return x * x
# def so_slow(num):
#     x = num
#     while x > 0:
#         x = x + 1
#     return x / 0

# square(so_slow(5))
## returns infinite loop

#1.4
def is_prime(n):
    for num in range(2,n-1):
        if n%num == 0:
            return False
    return True

#2.1
def keep_ints(cond, n):
    """Print out all integers 1..i..n where cond(i) is true
    >>> def is_even(x):
    ... # Even numbers have remainder 0 when divided by 2.
    ... return x % 2 == 0
    >>> keep_ints(is_even, 5)
    2
    4
    """

    for i in range(1,n):
        if cond(i) ==True:
            print(i)

#2.2
# >>> def outer(n):
# ...   def inner(m):
# ...       return n - m
# ... return inner
# >>> outer(61)
    #function inner
# >>> f = outer(10)
# >>> f(4)
    #6
# >>> outer(5)(4)
    #1

#2.3
def keep_ints_1(n):
    def num(conds):
        for i in range(1,n):
            if conds(i) ==True:
                print(i)
    return num



