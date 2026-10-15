def gen_fib():
    n, add = 0, 1
    while True:
        yield n
        n, add = n + add, n
#大于2026的最小斐波那契数, filter 自己会不断从 gen_fib() 里取值
next(filter(lambda n: n > 2026, t = gen_fib()))



def repeated(t, k):
    """Return the first value in iterator t that appears k times in a row,
    calling next on t as few times as possible.

    >>> s = iter([10, 9, 10, 9, 9, 10, 8, 8, 8, 7])
    >>> repeated(s, 2)
    9
    >>> t = iter([10, 9, 10, 9, 9, 10, 8, 8, 8, 7])
    >>> repeated(t, 3)
    8
    >>> u = iter([3, 2, 2, 2, 1, 2, 1, 4, 4, 5, 5, 5])
    >>> repeated(u, 3)
    2
    >>> repeated(u, 3)
    5
    >>> v = iter([4, 1, 6, 6, 7, 7, 8, 8, 2, 2, 2, 5])
    >>> repeated(v, 3)
    2
    """
    assert k > 1
    "*** YOUR CODE HERE ***"
    current = None
    happen = 1
    for i in t:     #for循环会自动调用next
        if i == current:
            happen += 1
            if happen == k:
                return i

        else:
            current = i
            happen = 1

def differences(t):
    """Yield the differences between adjacent values from iterator t.

    >>> list(differences(iter([5, 2, -100, 103])))
    [-3, -102, 203]
    >>> next(differences(iter([39, 100])))
    61
    """
    "*** YOUR CODE HERE ***"
    current = next(t)
    for i in t:
        yield i - current
        current = i

def partition_gen(n, m):
    """Yield the partitions of n using parts up to size m.
    >>> for partition in sorted(partition_gen(6, 4)):
    ...     print(partition)
    1 + 1 + 1 + 1 + 1 + 1
    1 + 1 + 1 + 1 + 2
    1 + 1 + 1 + 3
    1 + 1 + 2 + 2
    1 + 1 + 4
    1 + 2 + 3
    2 + 2 + 2
    2 + 4
    3 + 3
    """
    assert n > 0 and m > 0
    if n == m:
        yield [n]
    if n - m > 0:
        "*** YOUR CODE HERE ***"
        for p in partition_gen(n-m,m):
            yield p + [m]
    if m > 1:
        "*** YOUR CODE HERE ***"
        yield from partition_gen(n,m-1)


def squares(total, k):
    """Yield the ways in which perfect squares greater or equal to k*k sum to total.

    >>> list(squares(10, 1))  # All lists of perfect squares that sum to 10
    [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [4, 1, 1, 1, 1, 1, 1], [4, 4, 1, 1], [9, 1]]
    >>> list(squares(20, 2))  # Only use perfect squares greater or equal to 4 (2*2).
    [[4, 4, 4, 4, 4], [16, 4]]
    """
    assert total > 0 and k > 0
    if total - k*k == 0:
        return [[k*k]]

    if total < k*k:
        return []
    
    left = squares(total-k*k, k)
    for p in left:
        p.append(k*k)

    right = squares(total, k+1)

    return left + right

def squares(total, k):
    assert total > 0 and k > 0

    if k * k > total:
        return

    if k * k == total:
        yield [k * k]

    if k * k < total:
        for p in squares(total - k * k, k):
            yield p + [k * k]

    yield from squares(total, k + 1)

def church_generator(f):
    """Takes in a function f and yields functions which apply f
    to their argument one more time than the previously generated
    function.

    >>> increment = lambda x: x + 1
    >>> church = church_generator(increment)
    >>> for _ in range(5):
    ...     fn = next(church)
    ...     print(fn(0))
    0
    1
    2
    3
    4
    """
    g = lambda x: x
    while True:
        yield g
        g = lambda x, old_g=g: f(old_g(x))




        


