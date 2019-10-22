# 28122...12
# 6965 abundant numbers between 12 and 28122
# 1...11 = 66
# set membership: 1.9393091201782227 seconds
# list membership: 1333.623573064804 seconds
# set membership testing was 687.68 times faster than list membership

import time

t0 = time.time()

abundant_numbers = []
for number in range(1, 28123):
    divisor_count = 0
    check = number // 2
    while check > 0:
        if number % check == 0:
            divisor_count += check
        check -= 1
    if divisor_count > number:
        abundant_numbers.append(number)

abundant_numbers = set(abundant_numbers)

not_possibles = []
for i in range(28124):
    if i < 24:
        not_possibles.append(i)
    else:
        for j in abundant_numbers:
            if (j > i):
                not_possibles.append(i)
                break
            elif (i - j) in abundant_numbers:
                break
            elif (i / 2) in abundant_numbers:
                break
        else:
            not_possibles.append(i)

print(sum(not_possibles))

t1 = time.time()

total = t1-t0
print(total)
