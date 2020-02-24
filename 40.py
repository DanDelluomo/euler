Champernowne_Constant = "0.123456789"
count = 9

while len(Champernowne_Constant) < 1600007:
	count += 1
	Champernowne_Constant += str(count)

answer = int(Champernowne_Constant[2]) * int(Champernowne_Constant[11]) * int(Champernowne_Constant[101]) * int(Champernowne_Constant[1001]) * int(Champernowne_Constant[10001]) * int(Champernowne_Constant[100001]) * int(Champernowne_Constant[1000001])
print(answer)