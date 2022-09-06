""" Optional problems for Lab 6 """

## Nonlocal practice
def vending_machine(snacks):
    """Cycles through sequence of snacks.

    >>> vender = vending_machine(('chips', 'chocolate', 'popcorn'))
    >>> vender()
    'chips'
    >>> vender()
    'chocolate'
    >>> vender()
    'popcorn'
    >>> vender()
    'chips'
    >>> other = vending_machine(('brownie',))
    >>> other()
    'brownie'
    >>> vender()
    'chocolate'
    """
    "*** YOUR CODE HERE ***"
    count =0
    def cycle():
        nonlocal count
        if count == len(snacks):
            count = 1
            return snacks[count-1]
        else:
            #assignment of variable has to be before the increase of count
            item = snacks[count]
            count+=1
            return item
    return cycle
