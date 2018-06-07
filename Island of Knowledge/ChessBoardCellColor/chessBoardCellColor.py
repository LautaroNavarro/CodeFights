#By Lautaro Navarro

def chessBoardCellColor(cell1, cell2):
	if getColor(cell1) == getColor(cell2):
		return True
	else:
		return False
def getColor(cell):
	valores = {'A' : 0, 'B' : 1, 'C' : 2, 'D' : 3, 'E' : 4, 'F' : 5, 'G' : 6, 'H' : 7}
	posicionUno = valores[cell[0]]
	posicionDos = int(cell[1])
	if (posicionDos + posicionUno) % 2 == 0:
		return True
	else:
		return False