

from threading import main_thread


def tree(label, branches=[]):
    """Construct a tree with the given label value and a list of branches."""
    for branch in branches:
        assert is_tree(branch), 'branches must be trees'
    return [label] + list(branches)

def label(tree):
    """Return the label value of a tree."""
    return tree[0]

def branches(tree):
    """Return the list of branches of the given tree."""
    return tree[1:]

def is_tree(tree):
    """Returns True if the given tree is a tree, and False otherwise."""
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True

def is_leaf(tree):
    """Returns True if the given tree's list of branches is empty, and False
    otherwise.
    """
    return not branches(tree)

def print_tree(t, indent=0):
    """Print a representation of this tree in which each node is
    indented by two spaces times its depth from the root.

    >>> print_tree(tree(1))
    1
    >>> print_tree(tree(1, [tree(2)]))
    1
      2
    >>> numbers = tree(1, [tree(2), tree(3, [tree(4), tree(5)]), tree(6, [tree(7)])])
    >>> print_tree(numbers)
    1
      2
      3
        4
        5
      6
        7
    """
    print('  ' * indent + str(label(t)))
    for b in branches(t):
        print_tree(b, indent + 1)

def copy_tree(t):
    """Returns a copy of t. Only for testing purposes.

    >>> t = tree(5)
    >>> copy = copy_tree(t)
    >>> t = tree(6)
    >>> print_tree(copy)
    5
    """
    return tree(label(t), [copy_tree(b) for b in branches(t)])

#############
# Questions #
#############

def replace_leaf(t, old, new):
    """Returns a new tree where every leaf value equal to old has
    been replaced with new.

    >>> yggdrasil = tree('odin',
    ...                  [tree('balder',
    ...                        [tree('thor'),
    ...                         tree('loki')]),
    ...                   tree('frigg',
    ...                        [tree('thor')]),
    ...                   tree('thor',
    ...                        [tree('sif'),
    ...                         tree('thor')]),
    ...                   tree('thor')])
    >>> laerad = copy_tree(yggdrasil) # copy yggdrasil for testing purposes
    >>> print_tree(replace_leaf(yggdrasil, 'thor', 'freya'))
    odin
      balder
        freya
        loki
      frigg
        freya
      thor
        sif
        freya
      freya
    >>> laerad == yggdrasil # Make sure original tree is unmodified
    True
    """
    "*** YOUR CODE HERE ***"
    lst = []
    if is_leaf(t) and label(t) == old:
        return tree(new)
    else:
        for b in branches(t):
            lst.append(replace_leaf(b,old,new))
        return tree(label(t), lst)


    #the tree() function returns a tree lol

    
def print_move(origin, destination):
    """Print instructions to move a disk."""
    print("Move the top disk from rod", origin, "to rod", destination)

def move_stack(n, start, end):
    """Print the moves required to move n disks on the start pole to the end
    pole without violating the rules of Towers of Hanoi.

    n -- number of disks
    start -- a pole position, either 1, 2, or 3
    end -- a pole position, either 1, 2, or 3

    There are exactly three poles, and start and end must be different. Assume
    that the start pole has at least n disks of increasing size, and the end
    pole is either empty or has a top disk larger than the top n start disks.

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
    "*** YOUR CODE HERE ***"
    if n == 1:
        print_move(start, end)
        return
    aux = 6-start-end
    move_stack(n-1, start, aux)
    move_stack(1, start, end)
    move_stack(n-1, aux, end)
    
    #iterate down to n where it will just print out the move

###########
# Mobiles #
###########

def mobile(left, right):
    """Construct a mobile from a left side and a right side."""
    return tree('mobile', [left, right])

def is_mobile(m):
    return is_tree(m) and label(m) == 'mobile'

def sides(m):
    """Select the sides of a mobile."""
    assert is_mobile(m), "must call sides on a mobile"
    return branches(m)

def is_side(m):
    return not is_mobile(m) and not is_weight(m) and type(label(m)) == int

def side(length, mobile_or_weight):
    """Construct a side: a length of rod with a mobile or weight at the end."""
    return tree(length, [mobile_or_weight])

def length(s):
    """Select the length of a side."""
    assert is_side(s), "must call length on a side"
    return label(s)

def end(s):
    """Select the mobile or weight hanging at the end of a side."""
    assert is_side(s), "must call end on a side"
    return branches(s)[0]

def weight(size):
    """Construct a weight of some size."""
    assert size > 0
    "*** YOUR CODE HERE ***"
    return tree(size)

def size(w):
    """Select the size of a weight."""
    "*** YOUR CODE HERE ***"
    return label(w)

def is_weight(w):
    """Whether w is a weight, not a mobile."""
    "*** YOUR CODE HERE ***"
    # return type(size(w)) == int ?? Why dis wrong -- maybe is_weight always returning false so the total_weight if statement does not work 
    return is_leaf(w)
    

def examples():
    t = mobile(side(1, weight(2)),
               side(2, weight(1)))
    u = mobile(side(5, weight(1)),
               side(1, mobile(side(2, weight(3)),
                              side(3, weight(2)))))
    v = mobile(side(4, t), side(2, u))
    return (t, u, v)


def total_weight(m):
    """Return the total weight of m, a weight or mobile.

    >>> t, u, v = examples()
    >>> total_weight(t)
    3
    >>> total_weight(u)
    6
    >>> total_weight(v)
    9
    """
    if is_weight(m):
        return size(m)
    else:
        assert is_mobile(m), "must get total weight of a mobile or a weight"
        return sum([total_weight(end(s)) for s in sides(m)])

def balanced(m):
    """Return whether m is balanced.

    >>> t, u, v = examples()
    >>> balanced(t)
    True
    >>> balanced(v)
    True
    >>> w = mobile(side(3, t), side(2, u))
    >>> balanced(w)
    False
    >>> balanced(mobile(side(1, v), side(1, w)))
    False
    >>> balanced(mobile(side(1, w), side(1, v)))
    False
    """
    "*** YOUR CODE HERE ***"  
    if is_weight(m):
        return True
    lst = []
    torque_left = total_weight(end(sides(m)[0])) * length(sides(m)[0])
    torque_right = total_weight(end(sides(m)[1])) * length(sides(m)[1])
    for s in sides(m):  
        lst.append(torque_left == torque_right)
        lst.append(balanced(end(s)))
    return not False in lst

#######
# OOP #
#######

class Account:
    """An account has a balance and a holder.

    >>> a = Account('John')
    >>> a.deposit(10)
    10
    >>> a.balance
    10
    >>> a.interest
    0.02

    >>> a.time_to_retire(10.25) # 10 -> 10.2 -> 10.404
    2
    >>> a.balance               # balance should not change
    10
    >>> a.time_to_retire(11)    # 10 -> 10.2 -> ... -> 11.040808032
    5
    >>> a.time_to_retire(100)
    117
    """

    interest = 0.02  # A class attribute

    def __init__(self, account_holder):
        self.holder = account_holder
        self.balance = 0

    def deposit(self, amount):
        """Add amount to balance."""
        self.balance = self.balance + amount
        return self.balance

    def withdraw(self, amount):
        """Subtract amount from balance if funds are available."""
        if amount > self.balance:
            return 'Insufficient funds'
        self.balance = self.balance - amount
        return self.balance

    def time_to_retire(self, amount):
        """Return the number of years until balance would grow to amount."""
        assert self.balance > 0 and amount > 0 and self.interest > 0
        "*** YOUR CODE HERE ***"
        current_amount = self.balance
        years = 0 
        while current_amount < amount:
            current_amount = current_amount * 1.02
            years += 1
        return years




class FreeChecking(Account):
    """A bank account that charges for withdrawals, but the first two are free!

    >>> ch = FreeChecking('Jack')
    >>> ch.balance = 20
    >>> ch.withdraw(100)  # First one's free
    'Insufficient funds'
    >>> ch.withdraw(3)    # And the second
    17
    >>> ch.balance
    17
    >>> ch.withdraw(3)    # Ok, two free withdrawals is enough
    13
    >>> ch.withdraw(3)
    9
    >>> ch2 = FreeChecking('John')
    >>> ch2.balance = 10
    >>> ch2.withdraw(3) # No fee
    7
    >>> ch.withdraw(3)  # ch still charges a fee
    5
    >>> ch.withdraw(5)  # Not enough to cover fee + withdraw
    'Insufficient funds'
    """
    withdraw_fee = 1
    free_withdrawals = 2

    "*** YOUR CODE HERE ***"
    def withdraw(self, amount):
        if self.free_withdrawals > 0:
            self.free_withdrawals -= 1
            return super().withdraw(amount)
        else:
            amount += self.withdraw_fee
        return super().withdraw(amount)

############
# Mutation #
############

def make_counter():
    """Return a counter function.

    >>> c = make_counter()
    >>> c('a')
    1
    >>> c('a')
    2
    >>> c('b')
    1
    >>> c('a')
    3
    >>> c2 = make_counter()
    >>> c2('b')
    1
    >>> c2('b')
    2
    >>> c('b') + c2('b')
    5
    """
    "*** YOUR CODE HERE ***"
    storage = []
    def input(x):
        nonlocal storage
        storage.append(x)
        count = 0
        for s in storage:
            if s == x:
                count +=1
        return count
    return input

def make_fib():
    """Returns a function that returns the next Fibonacci number
    every time it is called.

    >>> fib = make_fib()
    >>> fib()
    0
    >>> fib()
    1
    >>> fib()
    1
    >>> fib()
    2
    >>> fib()
    3
    >>> fib2 = make_fib()
    >>> fib() + sum([fib2() for _ in range(5)])
    12
    """
    "*** YOUR CODE HERE ***"
    last_two_num = [0,1]
    num_calls = 0
    def input():
        nonlocal last_two_num
        nonlocal num_calls
        if num_calls == 0:
            num_calls+=1
            return 0
        elif num_calls == 1:
            num_calls+=1
            return 1
        else:
            last_two_num.append(sum(last_two_num))
            last_two_num.remove(last_two_num[0])
            return last_two_num[1]
    return input


def make_withdraw(balance, password):
    """Return a password-protected withdraw function.

    >>> w = make_withdraw(100, 'hax0r')
    >>> w(25, 'hax0r')
    75
    >>> error = w(90, 'hax0r')
    >>> error
    'Insufficient funds'
    >>> error = w(25, 'hwat')
    >>> error
    'Incorrect password'
    >>> new_bal = w(25, 'hax0r')
    >>> new_bal
    50
    >>> w(75, 'a')
    'Incorrect password'
    >>> w(10, 'hax0r')
    40
    >>> w(20, 'n00b')
    'Incorrect password'
    >>> w(10, 'hax0r')
    "Your account is locked. Attempts: ['hwat', 'a', 'n00b']"
    >>> w(10, 'l33t')
    "Your account is locked. Attempts: ['hwat', 'a', 'n00b']"
    >>> type(w(10, 'l33t')) == str
    True
    """
    "*** YOUR CODE HERE ***"
    balance = balance
    password = password
    wrong_pass = []

    def withdraw(amount, pas):
        nonlocal balance
        nonlocal password
        nonlocal wrong_pass
        if len(wrong_pass) == 3:
            return f"Your account is locked. Attempts: {wrong_pass}"
        elif pas != password:
            wrong_pass.append(pas)
            return 'Incorrect password'
        elif amount > balance:
           return 'Insufficient funds'
       
        balance = balance - amount
        return balance
    return withdraw

def make_joint(withdraw, old_password, new_password):
    """Return a password-protected withdraw function that has joint access to
    the balance of withdraw.

    >>> w = make_withdraw(100, 'hax0r')
    >>> w(25, 'hax0r')
    75
    >>> make_joint(w, 'my', 'secret')
    'Incorrect password'
    >>> j = make_joint(w, 'hax0r', 'secret')
    >>> w(25, 'secret')
    'Incorrect password'
    >>> j(25, 'secret')
    50
    >>> j(25, 'hax0r')
    25
    >>> j(100, 'secret')
    'Insufficient funds'

    >>> j2 = make_joint(j, 'secret', 'code')
    >>> j2(5, 'code')
    20
    >>> j2(5, 'secret')
    15
    >>> j2(5, 'hax0r')
    10

    >>> j2(25, 'password')
    'Incorrect password'
    >>> j2(5, 'secret')
    "Your account is locked. Attempts: ['my', 'secret', 'password']"
    >>> j(5, 'secret')
    "Your account is locked. Attempts: ['my', 'secret', 'password']"
    >>> w(5, 'hax0r')
    "Your account is locked. Attempts: ['my', 'secret', 'password']"
    >>> make_joint(w, 'hax0r', 'hello')
    "Your account is locked. Attempts: ['my', 'secret', 'password']"
    """
    "*** YOUR CODE HERE ***"
    
    response = withdraw(0, old_password)
    if type(response) == str:  #still mutates it just need to return the response LOl
        return response
    passwords = [old_password, new_password] # need to store the other new_password from before too. 
    def check(amount, password):
        nonlocal passwords
        if password in passwords:
            return withdraw(amount, passwords[0])
        else:
            return withdraw(amount, password)
    #hm they are adding the password to the checking process. 
    return check


###################
# Extra Questions #
###################

def interval(a, b):
    """Construct an interval from a to b."""
    return [a, b]

def lower_bound(x):
    """Return the lower bound of interval x."""
    "*** YOUR CODE HERE ***"
    return x[0]

def upper_bound(x):
    """Return the upper bound of interval x."""
    "*** YOUR CODE HERE ***"
    return x[1]

def str_interval(x):
    """Return a string representation of interval x."""
    return '{0} to {1}'.format(lower_bound(x), upper_bound(x))

def add_interval(x, y):
    """Return an interval that contains the sum of any value in interval x and
    any value in interval y."""
    lower = lower_bound(x) + lower_bound(y)
    upper = upper_bound(x) + upper_bound(y)
    return interval(lower, upper) #is this wrong?

def mul_interval(x, y):
    """Return the interval that contains the product of any value in x and any
    value in y."""
    p1 = lower_bound(x) * lower_bound(y)
    p2 = lower_bound(x) * upper_bound(y)
    p3 = upper_bound(x) * lower_bound(y)
    p4 = upper_bound(x) * upper_bound(y)
    return interval(min(p1, p2, p3, p4), max(p1, p2, p3, p4))

def sub_interval(x, y):
    """Return the interval that contains the difference between any value in x
    and any value in y."""
    "*** YOUR CODE HERE ***"
    p1 = lower_bound(x) - lower_bound(y)
    p2 = lower_bound(x) - upper_bound(y)
    p3 = upper_bound(x) - lower_bound(y)
    p4 = upper_bound(x) - upper_bound(y)
    return interval(min(p1, p2, p3, p4), max(p1, p2, p3, p4)) #I don't quite understand why its not like add...

def div_interval(x, y):
    """Return the interval that contains the quotient of any value in x divided by
    any value in y. Division is implemented as the multiplication of x by the
    reciprocal of y."""
    "*** YOUR CODE HERE ***"
    # I don't understand why it is -0.25 to 0.5 rather than -0.125 because that would be smallest
    assert upper_bound(y) < 0 or lower_bound(y) > 0
    reciprocal_y = interval(1/upper_bound(y), 1/lower_bound(y))
    return mul_interval(x, reciprocal_y) 

def par1(r1, r2):
    return div_interval(mul_interval(r1, r2), add_interval(r1, r2))

    # div_interval([1,2],[2,3] ) = 1/3, 1

def par2(r1, r2):
    one = interval(1, 1)
    rep_r1 = div_interval(one, r1)
    rep_r2 = div_interval(one, r2)
    return div_interval(one, add_interval(rep_r1, rep_r2))

    # rep_r1 = [1/2, 1]
    # rep_r2 = [1,1]
    # mul_interval([1,1], [1/2,2/3] ) = [1/2, 2/3]

def check_par():
    """Return two intervals that give different results for parallel resistors.

    >>> r1, r2 = check_par()
    >>> x = par1(r1, r2)
    >>> y = par2(r1, r2)
    >>> lower_bound(x) != lower_bound(y) or upper_bound(x) != upper_bound(y)
    True
    """
    r1 = interval(2, 1) # Replace this line!
    r2 = interval(1, 1) # Replace this line!
    #don't understand why
    return r1, r2

def multiple_references_explanation():
    return """The multiple reference problem... She is right because par1 refers
    to r1 and r2 - uncertain numbers - twice each in the mul_interval and add_interval parts. """

def quadratic(x, a, b, c):
    """Return the interval that is the range of the quadratic defined by
    coefficients a, b, and c, for domain interval x.

    >>> str_interval(quadratic(interval(0, 2), -2, 3, -1))
    '-3 to 0.125'
    >>> str_interval(quadratic(interval(1, 3), 2, -3, 1))
    '0 to 10'
    """
    "*** YOUR CODE HERE ***"
    def func(t):
        return a*t*t + b*t + c
         
    
    # doesn't just have to be whole numbers
    # integrate again to find if concave up or down, if a>0 then min point
    # if a< 0 then max point
    # still make sure that the extreme point is within the domain. 

    min_or_max = -b/(2*a)
    t1 = func(lower_bound(x))
    t2 = func(upper_bound(x))

    #smallest such interval to prevent multiple reference error?

    if a == 0:
        return interval(min(t1,t2), max(t1,t2))
    elif a>0:
        if min_or_max < upper_bound(x) and min_or_max > lower_bound(x):
            return interval(func(min_or_max), max(t1,t2))
        else:
            return interval(min(t1,t2), max(t1,t2))
    else:
        if min_or_max < upper_bound(x) and min_or_max > lower_bound(x):
            return interval(min(t1,t2), func(min_or_max))
        else:
            return interval(min(t1,t2), max(t1,t2))
    #remember, need to sub in the x value of extremem coordinate to get the Y value which is the range. 




        
import random
def polynomial(x, c):
    """Return the interval that is the range of the polynomial defined by
    coefficients c, for domain interval x.

    >>> str_interval(polynomial(interval(0, 2), [-1, 3, -2]))
    '-3 to 0.125'
    >>> str_interval(polynomial(interval(1, 3), [1, -3, 2]))
    '0 to 10'
    >>> str_interval(polynomial(interval(0.5, 2.25), [10, 24, -6, -8, 3]))
    '18.0 to 23.0'
    """
    "*** YOUR CODE HERE ***"
    def add_fn(coeff, k , f):
        return lambda x: coeff * pow(x, k) +f(x)
    def add_dfn(coeff, k, f):
        return lambda x: coeff * k * pow(x,k-1) + f(x)
    def add_ddfn(coeff, k, f):
        return lambda x: coeff * k * ( k-1) * pow(x, k-2) + f(x)
    f = lambda x: 0
    df = lambda x: 0
    dff = lambda x: 0
    for k,coeff in enumerate(c):
        f = add_fn(coeff,k,f)
        if k>0:
            df = add_dfn(coeff, k, df)
        if k>0:
            dff = add_ddfn(coeff, k, dff)

    
    # def add_fn(coeff, k, f):
    #     return lambda x: coeff * pow(x, k) + f(x)

    # def add_dfn(coeff, k, df):
    #     return lambda x: k * coeff * pow(x, k-1) + df(x)

    # def add_ddfn(coeff, k, ddf):
    #     return lambda x: k * (k-1) * coeff * pow(x, k-2) + ddf(x)

    # # Define the polynomial and its first and second derivatives.
    # f = lambda x: 0
    # df = lambda x: 0
    # ddf = lambda x: 0
    # for k, coeff in enumerate(c):
    #     # Actually it's a recursive call. It's a little bit different cause it's from bottom to top
    #     # as this statement processes, f updates ( and a new lambda func is defined every time this statement executed)
    #     f = add_fn(coeff, k, f)
    #     if k > 0:
    #         df = add_dfn(coeff, k, df)
    #     if k > 1:
    #         ddf = add_ddfn(coeff, k, ddf)


    # Newtons Method from Lecture
    def newton_update(f, df):
        def update(x):
            return x - f(x)/ df(x)
        return update
    
    def find_zero(f, df, guess = 1):
        def near_zero(x):
            return aprox_eq(f(x), 0)
        return improve(newton_update(f, df), near_zero, guess)

    def aprox_eq(num, close , ): 
        return abs(num - close) < 1e-15 #forgot to include part that returns false. 
            
    def improve(update, close, guess = 1, max_update = 100):
        k = 0
        while close(guess) == False and k < max_update:
            guess = update(guess)
            k += 1
        return guess

    
    #smallest such interval to prevent multiple reference error?
    low = lower_bound(x)
    up = upper_bound(x)
    num_steps = 20
    step = (up-low)/num_steps
    start = [ low + k* step for k in range(num_steps)]
    values = [ find_zero(df, dff, n) for n in start if n> low and n< up] 
    ns = [n for n in values if n> low and n< up] + [low,up]
    #could go lower than the actual if finding the closest extreme actually
    y_val = [f(n) for n in ns]
    return interval(min(y_val), max(y_val))



   

   


        
