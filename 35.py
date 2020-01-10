import math
CIRCULAR_PRIMES = 13

def prime_test(integer) -> bool:
    n = 2
    while n < int(math.sqrt(integer)):
        if integer % n == 0:
            return False
        n += 1
    return True

def circ_gen(integer, limit=1000000) -> bool:
    str_int = str(integer)
    iter_length = len(str_int)
    while iter_length > 0:
        str_int = str_int[1:] + str_int[0]
        if prime_test(int(str_int)) != True:
            return False
        iter_length -= 1
    return True

for i in range(100, 1000000):
    if circ_gen(i) == True:
        CIRCULAR_PRIMES += 1

print(CIRCULAR_PRIMES)