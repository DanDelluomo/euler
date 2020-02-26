a = 3000
pandigitals = []

def pandigits():
	global a
	num_string = str(a)

	# Pandigit Check.
	if len(num_string) == len(set(num_string)):
		sorted_num_string = [int(i) for i in num_string]
		sorted_num_string.sort()

		if sorted_num_string[0] == 1 and sorted_num_string[-1] == len(sorted_num_string):
			print('pandigital found: ', num_string)
			pandigitals.append(num_string)

		a -= 1

	# Not a pandigital, so lower a as much as possible.
	else:
		temp_set = set()
		for index, value in enumerate(num_string):
			if value not in temp_set:
				temp_set.add(value)
			else:

				# Lower a as much as possible.
				# If the duplicate is found at the end of the string, then just lower by 1.
				if index == len(num_string) - 1 or num_string[-1] == '0':
					a -= 1
					break
				else:
					lowered_number = num_string[:index + 1]
					# print('lowered_number ', lowered_number)
					for i in num_string[index + 1:]:
						lowered_number += '0'
					a = int(lowered_number)
					break


	print(a)


pandigits()
pandigits()
pandigits()
pandigits()
pandigits()


# while a > 2000:
# 	print(a)
# 	pandigit_check()




				
										
		