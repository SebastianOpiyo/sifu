def fib(n):
    dp = [0] * n
    dp[0], dp[1] = 0, 1

    for i in range(2, n):
        dp[i] = dp[i-1] + dp[i-2]

    return dp[-1]


def fibonacci(n):
    '''O(2^n)) -> Exponential'''

    if n <= 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


def fib_memoized(n, memo={}):
    '''Time - O(n), Space - O(n)'''

    if n <= 1:
        return 1

    if n in memo:
        return memo[n]

    memo[n] = fib_memoized(n - 1) + fib_memoized(n - 2)
    return memo[n]


def fib_iter(n):
    ''' O(n) time and O(1) space.'''

    if n < 0:
        raise IndexError('Negative Index 🌜')
    if n <= 1:
        return 1

    prev, curr = 0, 1
    for _ in range(n):
        prev, curr = curr, prev + curr

    return prev


assert fib_iter(5) == 5
assert fib_iter(6) == 8
assert fib_iter(7) == 13
