import prime_test
pandigit_list = []

checker = 4001

def pandigit_check():
    global checker
    num_string = str(checker) 
    sorted_num_string = [int(i) for i in num_string]
    sorted_num_string.sort()
    end = sorted_num_string[len(sorted_num_string) - 1]

    if len(num_string) == len(set(num_string)):
        checker -= 1
        if end - sorted_num_string[0] != len(sorted_num_string) - 1:
            # return False
            if num_string.find('0') != -1:
                 pass
            else:
                pandigit_list.append(num_string)
    else:
        print(checker)
        temp_set = set()
        for index, value in enumerate(num_string):
            if value not in temp_set:
                temp_set.add(value)
            else:
                new_num = num_string[:index - 1]
                for i in num_string[index:]:
                    new_num += '0'
                checker = int(new_num)
        

while checker > 2:
    print(checker)
    pandigit_check()

# print(pandigit_check)
    
