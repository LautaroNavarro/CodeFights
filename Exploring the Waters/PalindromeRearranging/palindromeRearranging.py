# By Lautaro Navarro

def palindromeRearranging(inputString):
	caracter = []
	for i in inputString:
		if inputString.count(i) % 2 != 0:
			if len(caracter) > 0 and caracter[0] != i:
				return False
			else:
				caracter.append(i)
	return True

# possible hidden test 
# input : 'anulalaluzazulalaluna'
# outpit: true