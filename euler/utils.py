from typing import List


def get_prime_factors(up_to: int) -> List[List[int]]:
    prime_factors = [[] for _ in range(up_to + 1)]

    for num in range(2, up_to + 1):
        if not prime_factors[num]:
            prime_factors[num] = [num]
            for i in range(2, up_to // num + 1):
                if not prime_factors[num * i]:
                    prime_factors[num * i] = [num, i]
    for num in range(2, up_to + 1):
        prime_factors[num] = [
            n
            for factor in prime_factors[num]
            for n in prime_factors[factor]
        ]

    return prime_factors


def get_primes_up_to(n: int):
    seen = set()
    primes = []
    for e in range(2, n + 1):
        if e not in seen:
            primes.append(e)
            seen.update(i * e for i in range(1, n // e + 1))
    return primes
