""" Optional problems for Lab 3 """

from lab03 import *

## Higher order functions

def cycle(f1, f2, f3):
    """Returns a function that is itself a higher-order function.

    >>> def add1(x):
    ...     return x + 1
    >>> def times2(x):
    ...     return x * 2
    >>> def add3(x):
    ...     return x + 3
    >>> my_cycle = cycle(add1, times2, add3)
    >>> identity = my_cycle(0)
    >>> identity(5)
    5
    >>> add_one_then_double = my_cycle(2)
    >>> add_one_then_double(1)
    4
    >>> do_all_functions = my_cycle(3)
    >>> do_all_functions(2)
    9
    >>> do_more_than_a_cycle = my_cycle(4)
    >>> do_more_than_a_cycle(2)
    10
    >>> do_two_cycles = my_cycle(6)
    >>> do_two_cycles(1)
    19
    """
    "*** YOUR CODE HERE ***"
    def cycle_amount(x):
        def user_input(y):
            list_of_functions = [f1,f2,f3]
            count = 0
            num = 0
            while count< x:
               if num>=3:
                    num = 0  
               y = list_of_functions[num](y)
               count +=1
               num+=1
            return y
        return user_input
    return cycle_amount
   
        
        

            
        



## Lambda expressions

def is_palindrome(n):
    """
    Fill in the blanks '_____' to check if a number
    is a palindrome.

    >>> is_palindrome(12321)
    True
    >>> is_palindrome(42)
    False
    >>> is_palindrome(2015)
    False
    >>> is_palindrome(55)
    True
    """
    x, y = n, 0
    f = lambda: x%10 + y*10
    while x > 0:
        x, y = x//10, f()
    return y == n
#takes remainder and adds previous remainderx10

## More recursion practice

def skip_mul(n):
    """Return the product of n * (n - 2) * (n - 4) * ...

    >>> skip_mul(5) # 5 * 3 * 1
    15
    >>> skip_mul(8) # 8 * 6 * 4 * 2
    384
    """
    if n <= 2:
        return n
    else:
        return n * skip_mul(n - 2)

def is_prime(n):
    """Returns True if n is a prime number and False otherwise.

    >>> is_prime(2)
    True
    >>> is_prime(16)
    False
    >>> is_prime(521)
    True
    """
    "*** YOUR CODE HERE ***"
    if n ==1:
        return False
    def check(i):
        if n== i:
            return True
        elif n%i == 0:
            return False
        else:
            check(i+1)
    check(2)


def interleaved_sum(n, odd_term, even_term):
    """Compute the sum odd_term(1) + even_term(2) + odd_term(3) + ..., up
    to n.

    >>> # 1 + 2^2 + 3 + 4^2 + 5
    ... interleaved_sum(5, lambda x: x, lambda x: x*x)
    29
    >>> #hi
    ... interleaved_sum(4, lambda x: x, lambda x: x*x)
    24
    """
    "*** YOUR CODE HERE ***"
    
    def helper_func(i,n, even_term,odd_term):
        if i == n+1: #if i==n we still want to run the recursion again, but for the last time
            return 0
        elif i < n:
            return helper_func(i+2, n,even_term,odd_term) + even_term(i) + odd_term(i+1)
        else:
            return helper_func(i+1, n, even_term, odd_term) + even_term(i)
        #remember we start from 0 so it is necessary to add the even_term that follows, if it is odd
        #then i == n+1 and the extra case will already be returned so it is good. 

    return helper_func(0,n,even_term, odd_term)



def ten_pairs(n):
    """Return the number of ten-pairs within positive integer n.

    >>> ten_pairs(7823952)
    3
    >>> ten_pairs(55055)
    6
    >>> ten_pairs(9641469)
    6
    """
    "*** YOUR CODE HERE ***"
    def helper_func(i, k):
        if k == 0:
            return 0
        elif i == (10-(k%10)):
            return 1+ helper_func(i, k//10)
        else:
            return helper_func(i, k//10)
    if n< 10:
        return 0 #don't call the function again after this because can't match with anything
    else:
        return helper_func(n%10, n//10) + ten_pairs(n//10)
    #basically checking each single digit with the rest of the code to see if it makes up a ten,
