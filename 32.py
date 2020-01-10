all_digits = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
pandigit_sums = set()
for i in range(1, 10000):
    for j in range(1, 1000):
        product = i * j
        pandigits = str(i) + str(j) + str(product)
        for digit in all_digits:
            if pandigits.count(digit) != 1:
                break
        else:
            if pandigits.count('0') == 0:
                pandigit_sums.add(int(product))

print(sum(pandigit_sums))