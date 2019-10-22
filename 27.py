new_dict = {

}
def longest_repeating(dict_index, string):
    global new_dict
    local_repeating = {
    }


    for index, value in enumerate(string[:25]):
        local_repeating[index] = value
        for j in local_repeating:
            if index != j:
                local_repeating[j] += value
            if string.find(local_repeating[j] * 7) != -1:
                new_dict[dict_index] = len(local_repeating[j])
                return

longest_repeating(0, "0.5142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857")
print(new_dict)
