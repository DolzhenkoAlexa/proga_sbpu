def sieve(n):
    is_prime = [True] * (n + 1)
    # Числа 0 и 1 не простые по определению просого
    is_prime[0] = False
    is_prime[1] = False
    
    for num in range(2, int(n ** 0.5) + 1):
        if is_prime[num]:
            for x in range(num * num, n + 1, num):
                is_prime[x] = False
                
    primes = []
    for i in range(n + 1):
        if is_prime[i]:
            primes.append(i)
    return primes


# Пример использования с n = 30
n = 30
primes = sieve(n)
print("Простые числа до", n, ":", primes)
