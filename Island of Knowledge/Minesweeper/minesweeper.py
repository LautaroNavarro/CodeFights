#By Lautaro Navarro

def minesweeper(Matrix):
	matrisResultante = []
	for i in range(0,len(Matrix)):
		matrisResultante.append([])
		for j in range(0,len(Matrix[0])):
			matrisResultante[i].append(0)
			for n in range( i -1, i + 2):
				for m in range(j - 1, j + 2):
					if n == i and m == j:
						pass
					else:
						if n < 0 or m < 0:
							pass
						else:
							try:
								if Matrix[n][m]:
									matrisResultante[i][j] += 1
							except Exception as e:
								pass
	return matrisResultante


