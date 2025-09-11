def fib(n):
    if n == 0:
        return 0
    prev, curr = 0, 1
    for i in range(n - 1):
        prev, curr = curr, prev + curr
    return curr

result = (fib(10**6 + 8) % 239)
print(result)