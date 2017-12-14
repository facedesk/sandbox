number = input("please enter a number")
length = len(number) #how many digits are in the number, 
			#how many times to loop

#12354
x = 0 #how many times have you looped
totalsum= 0 # 
while(x < length):
	numbertoadd = int(number[x]) #integer of each digit
	totalsum = totalsum + numbertoadd
	x=x+1
print(totalsum)

