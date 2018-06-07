#By Lautaro Navarro

import math

def boxBlur(image):
	array = []
	for x in range(1,len(image) - 1):
		array.append([])
		for i in range(1,len(image[x]) - 1):
			calculo = image[x-1][i-1] + image[x-1][i] + image[x-1][i + 1]
			calculo += image[x][i-1] + image[x][i] + image[x][i + 1]
			calculo += image[x+1][i-1] + image[x+1][i] + image[x+1][i + 1]
			array[x-1].append(math.floor(calculo/9))
	return array

#Note: You can use math.fsum but it affects the precision. It can fail with 
#	   big numbers