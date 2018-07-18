#By Lautaro Navarro

def firstDigit(inputString):
	for i in inputString:
		if i.isnumeric():
			return i
