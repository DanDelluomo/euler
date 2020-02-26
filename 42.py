triangle_numbers = []

for i in range(1, 100):
    triangle_num = int((0.5 * i) * (i + 1))
    triangle_numbers.append(triangle_num)

words = []
with open('files/p042_words.txt', 'r') as file:
    for line in file:
        for word in line.split(','):
            words.append(word)

value_map = {
    '"': 0,
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
    'Z': 26,
}

total_triangle_words = 0

for word in words:
    sum = 0
    for letter in word:
        sum += value_map[letter]
    if sum in triangle_numbers:
        total_triangle_words += 1

print(total_triangle_words)






