total_terms = []

for i in range(2, 101):
    for j in range(2, 101):
        total_terms.append(i ** j)

print(len(set(total_terms)))