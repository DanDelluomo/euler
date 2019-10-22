import time
t0 = time.time()


import sys
sys.setrecursionlimit(10000)

master_dict = {}

def long_division(dividend, divisor, zero_remainder=None):
    # base case
    if wrapper_long_div.count == 5000:
        master_dict[wrapper_long_div.num] = wrapper_long_div.quotient_string
        return

    if divisor > dividend:
        dividend = dividend * 10
        wrapper_long_div.quotient_string += str(dividend//divisor)
        wrapper_long_div.count += 1
        dividend = dividend - (dividend//divisor * divisor)
        if dividend == 0:
            return
        else:
            return long_division(dividend, divisor)
    else:
        wrapper_long_div.quotient_string += str(dividend//divisor)
        dividend = dividend - dividend//divisor
        wrapper_long_div.count += 1
        return long_division(dividend, divisor)


def wrapper_long_div(num):
    wrapper_long_div.num = num
    wrapper_long_div.quotient_string = "0."
    wrapper_long_div.count = 0
    long_division(1, num)


for i in range(2, 1000):
    wrapper_long_div(i)

def longest_repeating(dict_index, string):
    global new_dict
    local_repeating = {
    }


    for index, value in enumerate(string):
        local_repeating[index] = value
        for j in local_repeating:
            if index != j:
                local_repeating[j] += value
            if len(local_repeating[j]) > 30 and string.find(local_repeating[j] * 3) != -1:
                new_dict[dict_index] = len(local_repeating[j])
                return

new_dict = {}
for value in master_dict:
    longest_repeating(value, master_dict[value])

record = 0
record_tuple = None
for i in new_dict:
    if new_dict[i] > record:
        record = new_dict[i]
        record_tuple = (i, record)
print(record_tuple)

t1 = time.time()
total = t1-t0
print(total)
