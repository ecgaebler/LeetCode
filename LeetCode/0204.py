def countPrimes(n):
    primes = []
    for i in range(2, n):
        could_be_prime = True
        for prime in primes:
            if (i%prime) == 0: #i is not prime
                could_be_prime = False
                break
        if could_be_prime:
            primes.append(i)
    return len(primes)
