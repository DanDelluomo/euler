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


truncatable_primes = []
trunc_prime_test_int = 10

while len(truncatable_primes) < 11:
    print(trunc_prime_test_int)
    if str(trunc_prime_test_int)[0] in {'2', '3', '5', '7'} and str(trunc_prime_test_int)[-1] in {'3', '5', '7'}:
        if prime_test(trunc_prime_test_int) == True:
            tester_left = tester_right  = str(trunc_prime_test_int)
            tester_left_bool = tester_right_bool = True
            while len(tester_left) > 1:
                tester_left = tester_left[1:]
                if not prime_test(tester_left):
                    tester_left_bool = False
                    break
            while len(tester_right) > 1:
                tester_right = tester_right[:-1]
                if not prime_test(tester_right):
                    tester_right_bool = False
                    break
            if tester_left_bool and tester_right_bool:
                truncatable_primes.append(trunc_prime_test_int)

    trunc_prime_test_int += 1

print(sum(truncatable_primes))
