'''
a strong number is a number where the sum of the factorial of each digit is equal to the original number

- be able to calculate a factorial
- is final answer = original number
- find the sum of each factorial
- given a number, find each number as a digit
1456
1!    1
4!   24
5!  240
6! 1440
 _______
   1705
'''
strumber = input("please enter a number")
sum = 0
for strdigit in strumber:
	digit = int(strdigit)
	factorial = 1
	for multiplyMe in range(1,digit+1):
		factorial = factorial * multiplyMe
	print(strdigit+"! ="+str(factorial))
	sum = sum + factorial
if(int(strumber) == sum):
	print("the number is strong")
else:
	print("the number is not strong")
