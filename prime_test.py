import math

def prime_test(integer) -> bool:
    integer = int(integer)
    if integer in {0, 1}:
        return False
    if integer == 2:
        return True
    n = 2
    while n <= math.ceil(math.sqrt(integer)):
        if integer % n == 0:
            return False
        n += 1
    return True

