def make_keeper(n):
    """Returns a function that takes one parameter cond and prints
    out all integers 1..i..n where calling cond(i) returns True.

    >>> def is_even(x): # Even numbers have remainder 0 when divided by 2.
    ...     return x % 2 == 0
    >>> make_keeper(5)(is_even)
    2
    4
    >>> make_keeper(5)(lambda x: True)
    1
    2
    3
    4
    5
    >>> make_keeper(5)(lambda x: False)  # Nothing is printed
    """
    "*** YOUR CODE HERE ***"
    def function(cond):
        i = 1
        while i <= n:
            if cond(i):
                print(i)
            i += 1
    return function

def match_k(k):
    """Returns a function that checks if digits k apart match.

    >>> match_k(2)(1010)
    True
    >>> match_k(2)(2010)
    False
    >>> match_k(1)(1010)
    False
    >>> match_k(1)(1)
    True
    >>> match_k(1)(2111111111111111)
    False
    >>> match_k(3)(123123)
    True
    >>> match_k(2)(123123)
    False
    """
    def match(n):
        while n >= 10 ** k:
            current = n % 10
            other = (n // (10 ** k)) % 10

            if current != other:
                return False

            n //= 10

        return True

    return match




def ramp(n):
    """Return whether non-negative integer N has more increases than decreases.

    >>> ramp(123)   # 2 increases (1-> 2, 2-> 3) and 0 decreases
    True
    >>> ramp(1315)  # 2 increases (1-> 3, 1-> 5) and 1 decrease (3-> 1)
    True
    >>> ramp(176)   # 1 increase (1-> 7) and 1 decrease (7-> 6)
    False
    >>> ramp(5)     # 0 increases and 0 decreases
    False
    """
    down = 0
    up = 0
    save = n % 10
    while n > 0:
        current, n = n % 10, n // 10
        if current > save:
            down += 1
        elif current < save:
            up += 1

        save = current
    if up > down:
        return True
    else:
        return False


def process(n, tally, result):
    """Process all pairs of adjacent digits in N using functions TALLY and RESULT.
    """ 

    while n >= 10:
        tally, result = tally(n % 100 // 10, n % 10)
        n = n // 10
    return result()

def ups(k):
    """Return tally and result functions that compute whether N has exactly K increases.

    >>> f, g = ups(3)
    >>> process(1200849, f, g)    # Exactly 3 increases: 1 -> 2, 0 -> 8, 4 -> 9
    True
    >>> process(94004, f, g)      # 1 increase: 0 -> 4
    False
    >>> process(122333445, f, g)  # 4 increases: 1 -> 2, 2 -> 3, 3 -> 4, 4 -> 5
    False
    >>> process(0, f, g)          # 0 increases
    False
    """
    def tally(left, right):
        if left < right:
            return ups(k-1)
        elif left > right:
            return ups(k)

    def result():
        if k == 0:
            return True
        else:
            return False

    return tally, result


def only(n, t):
    """Return only the digits of n for which t returns True when called on each digit

    >>> only(23344567, lambda d: d % 2 == 0)
    2446
    >>> only(987654349675, lambda d: d < 7)
    6543465
    >>> only(2023, lambda d: False)
    0
    """
    total, i = 0, 0
    while n > 0:
        n, current = n // 10, n % 10
        if t(current):
            total += current * pow(10,i)
            i += 1
    return total


def every(t):
    """Return a function that returns whether t is True 
    for every digit of non-negative n.

    >>> f = every(lambda d: d % 2 == 1)
    >>> f(37511)  # every digit is odd
    True
    >>> f(2023)   # Not every digit is odd
    False
    """
    def digit(n):
        while n > 0:
            current, n = n % 10, n // 10
            if not t(current):
                return False

        return True
    return digit
