import math
factorial_curious_numbers = []

for i in range(10, 100000):
    factorial_sum = 0
    for j in str(i):
        factorial_sum += math.factorial(int(j))
    if factorial_sum == i:
        factorial_curious_numbers.append(i)

print(sum(factorial_curious_numbers))