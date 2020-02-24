# a = 3000

# def pandigits():
# 	global a
# 	num_string = str(a)
# 	if num_string.find('0') != -1:
# 		a -= 1
# 		return 
# 	else:
# 		if len(num_string) == len(set(num_string)):
# 			a -= 1
# 			return
# 		else:
# 			temp_set = set()
# 			reducer = False
# 			for index, value in enumerate(num_string):
# 				if value not in temp_set:
# 						temp_set.add(value)
# 				else:
# 					if value == '0':
# 						a -= 1
# 						break
# 					elif index == len(num_string) - 1:
# 						a -= 1
# 						break
# 					else:
# 						new_num = num_string[:index - 1]
# 						for i in num_string[index:]:
# 								new_num += '0'
# 						new_num += '0'
# 						a = int(new_num)


# pandigits()
# pandigits()
# pandigits()


# while a > 2000:
# 	pandigit_check()
# 	print(a)


class Solution:
	def checkPerfectNumber(self, num: int) -> bool:
  	divisors = set()
		if num < 3:
					return False
			
			for i in range(1, int(num**0.5) + 1):
					if num % i == 0:
							if num % i !== num:
									divisors.add(i)

			return sum(divisors) == num
				
										
		