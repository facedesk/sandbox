sunny = input("is it sunny? y/n")
hour = input("what is the hour of day?")
hour = int(hour)

'''
if it is sunny outside and the hour is between 4 and 8, then print the squirrels 
are playing outside

otherwise, print that they are sleeping

'''

isSunnyOutside = sunny == "y"
isBetween4and8 = hour >=4 and hour <=8

print(type(isSunnyOutside))
print(isBetween4and8)

if(isSunnyOutside and isBetween4and8):
	print("the squirrels are playing outside")
else:
	print("the squirrels are sleeping")


