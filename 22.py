letter_values = {
    'A': 1,
    'B': 2,
    'C': 3,
    'D': 4,
    'E': 5,
    'F': 6,
    'G': 7,
    'H': 8,
    'I': 9,
    'J': 10,
    'K': 11,
    'L': 12,
    'M': 13,
    'N': 14,
    'O': 15,
    'P': 16,
    'Q': 17,
    'R': 18,
    'S': 19,
    'T': 20,
    'U': 21,
    'V': 22,
    'W': 23,
    'X': 24,
    'Y': 25,
    'Z': 26
}

with open('files/names.txt') as f:
    name_list = f.read().split('","')
    new_list = [name.replace('"', '') for name in name_list]
    new_list.sort()
    total_sum = 0
    for index, name in enumerate(new_list):
        name_sum = 0
        for letter in name:
            name_sum += letter_values[letter]
        total_sum += (index + 1) * name_sum
    print(total_sum)
