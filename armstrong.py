'''
+given a number, how many digits does it have?
+find a digit
+raise a number to a power
+find sum of digits powered
+compare final answer to original number
'''


def is_armstrong(number):
	strumber = str(number)
	numberOfDigits = len(strumber)
	sum = 0

	for strdigit in strumber:
		digit = int(strdigit)
		sum = sum + (digit**numberOfDigits)
	if(sum == int(strumber)):
		#print("Wow, "+strumber+" actually is a armstrong number")
		return True
	else:
		#print(strumber + " is pretty armweak")
		return False
def generate_armstrong_numbers(highend):
	for x in range(highend):
		armstrong = is_armstrong(x)
		if(armstrong == True):
			print(str(x) + "is an armstrong number")

generate_armstrong_numbers(100000)
generate_armstrong_numbers(10)
