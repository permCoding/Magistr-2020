# 1 2 3 4 5 6 7  8
# 1 1 2 3 5 8 13 21 34

def get_fib(n):
    if n < 3:
        return 1
    else:
        return get_fib(n-1) + get_fib(n-2)


def get_fib_mem(n):
    # global fibs # список передаётся по ссылке ;)
    if n < 3:
        return 1
    else:
        if fibs[n - 1] == 0:
            fibs[n - 1] = get_fib_mem(n - 1)
        if fibs[n - 2] == 0:
            fibs[n - 2] = get_fib_mem(n - 2)
        return fibs[n - 1] + fibs[n - 2]


n = 136
fibs = [0] * n
# [0, 1, 1, 0, 0, 0]

print(get_fib_mem(n))
