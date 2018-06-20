#By Lautaro Navarro

def extractEachKth(inputArray, k):
	newArray =[]
	contador = 0
	for i in range(0,len(inputArray)):
		contador += 1
		if contador !=  k:
			newArray.append(inputArray[i])
		else:
			contador = 0
	return newArray