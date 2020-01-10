from functools import reduce
curious_fractions = []

for numerator in range(10,100):
    for denominator in range(10, 100):
        if denominator > numerator:
            string_glob = str(numerator) + str(denominator)
            if string_glob.count('0') == 0:
                if str(numerator)[1] == str(denominator)[0]:
                    canceled_form = int(str(numerator)[0]) / int(str(denominator)[1])
                    if canceled_form == (numerator / denominator):
                        curious_fractions.append((numerator / denominator))

print(reduce((lambda x, y: x * y), curious_fractions))