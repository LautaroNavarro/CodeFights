# By Lautaro Navarro

def arrayChange(inputArray):
    contador = 0
    for i in range(len(inputArray) - 1):
        if inputArray[i] >= inputArray[i+1]:
            contador += (inputArray[i] - inputArray[i+1]) + 1
            inputArray[i+1] += (inputArray[i] - inputArray[i+1]) + 1
    return contador