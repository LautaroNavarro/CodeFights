#By Lautaro Navarro

def absoluteValuesSumMinimization(a):
	largo = len(a)
	mitad = largo/2
	if largo %2 == 0:
		return int(a[int(mitad -1)] )
	else:
		return int(a[int(mitad)])
