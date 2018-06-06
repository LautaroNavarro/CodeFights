#By Lautaro Navarro

def avoidObstacles(inputArray):
	steap = 1
	while True:
		found = True
		for i in range (len(inputArray)):
			if inputArray[i] % steap == 0:
				found = False
				steap += 1
				break
		if found:
			break
	return steap

#Help: 
#	  You just have to find the smallest number that is 
#	  not a multiple of any vector element!