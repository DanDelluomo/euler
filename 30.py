fifth_powers_list = []

for i in range(2, 300000):
    string_i = str(i)
    sum_string_i = 0
    for j in string_i:
        sum_string_i += int(j)**5
    if sum_string_i == i:
        fifth_powers_list.append(i)

print(sum(fifth_powers_list))