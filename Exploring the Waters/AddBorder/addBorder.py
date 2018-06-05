# By Lautaro Navarro

def addBorder(picture):
	simbols = ''
	for x in range(len(picture[0]) + 2):
		simbols += '*'
	for x in range(len(picture)):
		picture[x] = '*' + picture[x]
		picture[x] = picture[x] + '*'
	picture.insert(0,simbols)
	picture.append(simbols)
	return picture