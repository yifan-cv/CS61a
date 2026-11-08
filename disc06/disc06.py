def gen_fib():
    n, add = 0, 1
    while True:
        yield n
        n, add = n + add, n
#大于2026的最小斐波那契数, filter 自己会不断从 gen_fib() 里取值
next(filter(lambda n: n > 2026, t = gen_fib()))





        


