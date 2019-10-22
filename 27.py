import math

def prime_test(num):
    for i in range(2, math.ceil(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

primes = [x for x in range(2,100000) if prime_test(x) == True or x == 2]
primes = set(primes)
record = 0
record_tuple_mult = None

for i in range(-1000,1001):
    for j_val in range(-1000,1001):
        max_primes = 0
        test_val = 0
        while test_val ** 2 + test_val * i + j_val in primes:
            test_val += 1
            max_primes += 1
        if max_primes > record:
            record = max_primes
            record_tuple_mult = i * j_val

print(record_tuple_mult)
