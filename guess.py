number = input("enter a number")
number = int(number)

secret = 21

if(number > secret):
    print("too high")
elif(number < secret):
    print("too low")
else:
    print("you got it!")


