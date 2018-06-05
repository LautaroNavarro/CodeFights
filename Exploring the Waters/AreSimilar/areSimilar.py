# By Lautaro Navarro

def areSimilar(a, b):
	sideA = []
	sideB = []
	for x in range(len(a)):
		if (a[x] != b[x]):
			sideA.append(a[x]) 
			sideB.append(b[x])
	if len(sideA) == 0:
		return True
	if len(sideA) > 2:
		return False
	else:
		return sideA == list(reversed(sideB))