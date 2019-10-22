
# Find the biggest i such that a[i] < a[i + 1];
# Find the biggest j greater than i such that a[j] > a[i];
# Swap a[i] and a[j];
# Reverse the elements from a[i + 1] to the last element.

# 012
# 021
# 102
# 120
# 201
# 210

import time
t0 = time.time()


lex = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
perm_count = 0
current_perm = lex
while perm_count < 999999:
    biggest_i = None
    for index, value in enumerate(current_perm[:-1]):
        if value < current_perm[index + 1]:
            biggest_i = index
    biggest_j = None
    for index1, value1 in enumerate(current_perm[biggest_i:]):
        if value1 > current_perm[biggest_i]:
            biggest_j = index1 + biggest_i
    current_perm[biggest_i], current_perm[biggest_j] = current_perm[biggest_j], current_perm[biggest_i]
    beginning = current_perm[:biggest_i + 1]
    ending = current_perm[biggest_i + 1:]
    ending.reverse()
    current_perm = beginning + ending
    perm_count += 1
print(current_perm)

t1 = time.time()
total = t1-t0
print(total)
