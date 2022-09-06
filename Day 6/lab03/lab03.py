""" Lab 3: Recursion and Midterm Review """

def gcd(a, b):
    """Returns the greatest common divisor of a and b.
    Should be implemented using recursion.

    >>> gcd(34, 19)
    1
    >>> gcd(39, 91)
    13
    >>> gcd(20, 30)
    10
    >>> gcd(40, 40)
    40
    """
    "*** YOUR CODE HERE ***"
    if a ==b:
        return a
    elif a < b :
        return gcd(b,a)
    else:
        return gcd(a-b,b)
    #euclidian algorithm
    
def trace(fn):
    def traced(x):
        print('applying', x, 'to', fn)
        return fn(x)
    return traced


def hailstone(n, count=1):
    """Print out the hailstone sequence starting at n, and return the
    number of elements in the sequence.

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
    """
    "*** YOUR CODE HERE ***"
    n = int(n)
    if n ==1:
        print(n)
        return count
    elif n %2 ==0 :
        print(n)
        return hailstone(n/2, count +1)
    else:
        print(n)
        return hailstone( 3*n +1, count+1)
