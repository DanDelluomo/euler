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

def permutations(string: str) -> list:

    all_permutations = []
    def permuter(items: list, current_string: str):
        if len(current_string) == len(items):
            all_permutations.append(current_string)
        else:
            for i in items:
                if i not in current_string:
                    new_string = current_string + i
                    permuter(items, new_string)

    pandigits = '123456789'
    while len(pandigits) > 2:
        permuter(list(pandigits), '')
        pandigits = pandigits[:-1]

    all_permutations = [int(i) for i in all_permutations]
    all_permutations.sort()
    return all_permutations

a = permutations('123456789')
for i in reversed(a):
    if prime_test(i):
        print(i)
        break