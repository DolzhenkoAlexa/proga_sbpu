def sieve(n):
    if n < 2:
        return []

    primes = [2]

    for num in range(3, n + 1, 2):
        limit = int(num ** 0.5) + 1
        for p in primes:
            if p > limit:
                primes.append(num)
                break
            if num % p == 0:
                break
        else:
            primes.append(num)
    return primes

n = int(input("Введите n (до которого хотите увидеть числа): "))
result = sieve(n)
print(f"Простые числа до n: {result}")