import math
primes = [2]
twice_squares = []
odd_composites = []

def prime_test(num):
    for i in range(2, math.ceil(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

for i in range(3, 100000, 2):
    if prime_test(i):
        primes.append(i)
    else:
        odd_composites.append(i)

for i in range(1, 1000000):
    i_sq = i * i
    twice_i_sq = 2 * i_sq
    twice_squares.append(twice_i_sq)

set_twice_squares = set(twice_squares)

for odd_comp in odd_composites:
    test = False
    for prime in primes:
        if prime >= odd_comp:
            break
        diff = odd_comp - prime
        if diff in set_twice_squares:
            test = True
    if test == False:
        print(f"The answer is {odd_comp}")
        break