def find_all_strings(string: str) -> list:
    strings = []
    for index, value in enumerate(string):
        substring = value
        for i in string[index + 1:]:
            substring += i
            strings.append(substring)
    print(strings)


find_all_strings('abcdefghijklmnop')
