cache = {}


def fib(n):
    global cache
    if n in cache:
        ans = cache[n]
    elif n <= 2:
        ans = 1
        cache[n] = 1
    else:
        ans = fib(n-1) + fib(n-2)
        cache[n] = ans
    return ans

def summer():
    n = 0
    sum = 0
    while fib(n) < 4000000:
        if fib(n) % 2 == 0:
            sum += fib(n)
        n += 1
    return sum

print(summer())