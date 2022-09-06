HW_SOURCE_FILE = 'hw04.py'

###############
#  Questions  #
###############
from math import sqrt

def intersection(st, ave):
    """Represent an intersection using the Cantor pairing function."""
    return (st+ave)*(st+ave+1)//2 + ave

def street(inter):
    return w(inter) - avenue(inter)

def avenue(inter):
    return inter - (w(inter) ** 2 + w(inter)) // 2

w = lambda z: int(((8*z+1)**0.5-1)/2)

def taxicab(a, b):
    """Return the taxicab distance between two intersections.

    >>> times_square = intersection(46, 7)
    >>> ess_a_bagel = intersection(51, 3)
    >>> taxicab(times_square, ess_a_bagel)
    9
    >>> taxicab(ess_a_bagel, times_square)
    9
    """
    "*** YOUR CODE HERE ***"
    return abs(street(a) - street(b)) + abs(avenue(a) - avenue(b))


def squares(s):
    """Returns a new list containing square roots of the elements of the
    original list that are perfect squares.

    >>> seq = [8, 49, 8, 9, 2, 1, 100, 102]
    >>> squares(seq)
    [7, 3, 1, 10]
    >>> seq = [500, 30]
    >>> squares(seq)
    []
    """
    "*** YOUR CODE HERE ***"
    # list_of_perfect_squares = []
    # for i in s:
    #     if sqrt(i)%1 == 0:
    #         list_of_perfect_squares.append(int(sqrt(i)))
    # return list_of_perfect_squares

    return [round(i**0.5) for i in s if i**0.5 == round(i**0.5)]
    

def g(n):
    """Return the value of G(n), computed recursively.

    >>> g(1)
    1
    >>> g(2)
    2
    >>> g(3)
    3
    >>> g(4)
    10
    >>> g(5)
    22
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'g', ['While', 'For'])
    True
    """
    "*** YOUR CODE HERE ***"
    if n<=3:
        return n
    elif n>3:
        return g(n - 1) + 2 * g(n - 2) + 3 * g(n - 3) 



def g_iter(n):
    """Return the value of G(n), computed iteratively.

    >>> g_iter(1)
    1
    >>> g_iter(2)
    2
    >>> g_iter(3)
    3
    >>> g_iter(4)
    10
    >>> g_iter(5)
    22
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'g_iter', ['Recursion'])
    True
    """
    "*** YOUR CODE HERE ***"
    data = [1,2,3]
    for i in range(3,n):
        data.append(data[i-1] + 2*data[i-2] + 3*data[i-3])
    return data[n-1]

    #keeps on adding on to the list so that can be accessed later on, 
            


def pingpong(n):
    """Return the nth element of the ping-pong sequence.

    >>> pingpong(7)
    7
    >>> pingpong(8)
    6
    >>> pingpong(15)
    1
    >>> pingpong(21)
    -1
    >>> pingpong(22)
    0
    >>> pingpong(30)
    6
    >>> pingpong(68)
    2
    >>> pingpong(69)
    1
    >>> pingpong(70)
    0
    >>> pingpong(71)
    1
    >>> pingpong(72)
    0
    >>> pingpong(100)
    2
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'pingpong', ['Assign', 'AugAssign'])
    True
    """
    "*** YOUR CODE HERE ***"
    # def helper_func(i, prev, count):
    #     if has_seven(count) or (count%7 ==0 and count != 0):
    #         if i> prev:
    #             if count == n:
    #                 return i
    #             return helper_func(i-1, i, count+1)
    #         if i<prev:
    #             if count == n:
    #                 return i
    #             return helper_func(i+1,i, count+1)
    #     else:
    #         if i> prev:
    #             if count == n:
    #                 return i
    #             return helper_func(i+1, i, count+1)
    #         if i<prev:
    #             if count == n:
    #                 return i
    #             return helper_func(i-1,i, count+1)
    # return helper_func(0,-1,0)
            
    #more concise version:
    def helper_func(count,num, inc):
        if count == n:
            return num
        elif has_seven(count) or count%7==0:
            return helper_func(count+1, num - inc, -inc)
        else:
            return helper_func(count+1, num+inc, inc)
    return helper_func(1,1,1)


def has_seven(k):
    """Returns True if at least one of the digits of k is a 7, False otherwise.

    >>> has_seven(3)
    False
    >>> has_seven(7)
    True
    >>> has_seven(2734)
    True
    >>> has_seven(2634)
    False
    >>> has_seven(734)
    True
    >>> has_seven(7777)
    True
    """
    if k % 10 == 7:
        return True
    elif k < 10:
        return False
    else:
        return has_seven(k // 10)

def count_change(amount):
    """Return the number of ways to make change for amount.

    >>> count_change(7)
    6
    >>> count_change(10)
    14
    >>> count_change(20)
    60
    >>> count_change(100)
    9828
    """
    "*** YOUR CODE HERE ***"
    def mul_2(num):
        i = 1
        while i<=num:
            i = i*2
        return i//2
    def partition(n, m):
        if n == 0:
            return 1
        elif n< 0:
            return 0
        elif m == 0:
            return 0
        else:
            return partition(n-m,m) + partition(n,m//2)
    return partition(amount, mul_2(amount))

###################
# Extra Questions #
###################

from operator import sub, mul

def make_anonymous_factorial():
    """Return the value of an expression that computes factorial.

    >>> make_anonymous_factorial()(5)
    120
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'make_anonymous_factorial', ['Assign', 'AugAssign', 'FunctionDef', 'Recursion'])
    True
    """
    # return lambda x: (i for i in [i for i in range(1,x)])
    #recursive lambda - learned how to call lambdas 
    return lambda b: (lambda a,b : a(a,b))((lambda a,b: b*a(a,b-1) if b>0 else 1), b) 
    
