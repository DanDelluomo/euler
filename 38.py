import math
max_solutions = (0, None)

for i in range(2, 1001, 2):
    solutions = 0
    for j in range(1, int(i/3)):
        remainder = math.ceil((i - j) / 2)
        for k in range(j, remainder):
            l = math.sqrt( (j ** 2) + (k ** 2) )
            if j + k + l == i:
                solutions += 1

    if solutions > max_solutions[0]:
        max_solutions = (solutions, i)

print(max_solutions)
