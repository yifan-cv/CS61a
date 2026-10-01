#Q1: Insect Combinatorics
def paths(m, n):
    """Return the number of paths from one corner of an
    M by N grid to the opposite corner.

    >>> paths(2, 2)
    2
    >>> paths(5, 7)
    210
    >>> paths(117, 1)
    1
    >>> paths(1, 157)
    1
    """
    "*** YOUR CODE HERE ***"
    def helper(x,y):
        if x == m and y == n:
            return 1
        elif x > m:
            return 0
        elif y > n:
            return 0
        return helper(x+1, y) + helper(x, y+1)
    return helper(1,1)


#Q2: Max Product
def max_product(s):
    """Return the maximum product of non-consecutive elements of s.

    >>> max_product([10, 3, 1, 9, 2])   # 10 * 9
    90
    >>> max_product([5, 10, 5, 10, 5])  # 5 * 5 * 5
    125
    >>> max_product([])                 # The product of no numbers is 1
    1
    """
    "*** YOUR CODE HERE ***"
    def helper(s):
        if s == []:
            return 1
        
        return max(s[-1] * helper(s[:-2]),helper(s[:-1]))  #子问题返回后，上一层继续拿这个数字返回
    return helper(s)

#Q3: Sum Fun
def sums(n, m):
    """Return lists that sum to n containing positive numbers up to m that
    have no adjacent repeats.

    >>> sums(5, 1)
    []
    >>> sums(5, 2)
    [[2, 1, 2]]
    >>> sums(5, 3)
    [[1, 3, 1], [2, 1, 2], [2, 3], [3, 2]]
    >>> sums(5, 5)
    [[1, 3, 1], [1, 4], [2, 1, 2], [2, 3], [3, 2], [4, 1], [5]]
    >>> sums(6, 3)
    [[1, 2, 1, 2], [1, 2, 3], [1, 3, 2], [2, 1, 2, 1], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
    """
    def prepend(k, lists):
        if lists == []:
            return []
        return [[k] + lists[0]] + prepend(k, lists[1:])

    def helper(total, previous, k):
        if total == 0:
            return [[]]

        if k > m:
            return []

        # 不选择 k，继续尝试下一个候选
        skip = helper(total, previous, k + 1)

        # k 太大，或者和上一个数字相同，不能选
        if k > total or k == previous:
            return skip

        # 选择 k
        rest = helper(total - k, k, 1)
        take = prepend(k, rest)

        return take + skip

    return helper(n, 0, 1)


#Q4: A Perfect Question
def fit(total, n):
    """Return whether there are n positive perfect squares that sums to total.

    >>> [fit(4, 1), fit(4, 2), fit(4, 3), fit(4, 4)]  # 1*(2*2) for n=1; 4*(1*1) for n=4
    [True, False, False, True]
    >>> [fit(12, n) for n in range(3, 8)]  # 3*(2*2), 3*(1*1)+3*3, 4*(1*1)+2*(2*2)
    [True, True, False, True, False]
    >>> [fit(32, 2), fit(32, 3), fit(32, 4), fit(32, 5)] # 2*(4*4), 3*(1*1)+2*2+5*5
    [True, False, False, True]
    """
    def helper(total, n, k):
        if total == 0 and n == 0:
            return True

        if total <= 0 or n == 0:
            return False

        if total < k * k:
            return False

        return (
            helper(total - k * k, n - 1, k)
            or
            helper(total, n, k + 1)
        )

    return helper(total, n, 1)



       