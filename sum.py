add_again = "y"
sum = 0
while(add_again == "y"):
	num1 = input("Please enter a number")
	num1 = int(num1)
	sum = sum + num1
	print(sum)
	print("Add again? y or n")
	add_again = input()
	
