import time

#5 minutes
#5,0,0
#4,5,9
hours = input("enter number of hours")
hours= int(hours)

for h1 in range(hours):
	for m1 in range(6):
		for m2 in range(10):
			for s2 in range(6):
				for s3 in range(10):
					print(h1,":",m1,m2,":",s2,s3)
					time.sleep(.0001)
