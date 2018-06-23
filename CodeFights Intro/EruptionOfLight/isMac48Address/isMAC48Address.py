#By Lautaro Navarro

def isMAC48Address(inputString):
	if len(inputString) != 17:
		return False
	inputString = inputString.replace("-","")
	if len(inputString) != 12:
		return False
	for i in range(len(inputString)):
		if not (ord(inputString[i]) >= 48 and ord(inputString[i]) <= 57 or ord(inputString[i]) >= 65 and ord(inputString[i]) <= 70):
			return False
	return True