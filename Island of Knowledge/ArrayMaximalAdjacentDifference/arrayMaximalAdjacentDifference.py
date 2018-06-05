#By Lautaro Navarro

def arrayMaximalAdjacentDifference(inputArray):
    maxDifference = 0
    for i  in range(1 , len(inputArray) - 1):
        if  abs((inputArray[i]) - (inputArray[i + 1])) > maxDifference:
            maxDifference = abs((inputArray[i]) - abs(inputArray[i + 1]))
        if  abs((inputArray[i]) - (inputArray[i -1 ])) > maxDifference:
            maxDifference = abs((inputArray[i]) - abs(inputArray[i - 1]))
    return maxDifference