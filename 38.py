def checker(concat_number) -> bool:
    if '0' in concat_number:
        return False
    for i in '123456789':
        if concat_number.count(i) != 1:
            return False
    return True

pandigit_multiples = []
for i in range(1, 10000):
    pandigits = str(i)
    for j in range(2, 9):
        pandigits += str(i * j)
        if checker(pandigits):
            pandigit_multiples.append(int(pandigits))

print(max(pandigit_multiples))