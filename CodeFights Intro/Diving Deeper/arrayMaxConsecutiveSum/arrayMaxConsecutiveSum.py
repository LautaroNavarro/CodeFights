#By Lautaro Navarro

def arrayMaxConsecutiveSum(inputArray, k):
    sumas = []
    for i in range(len(inputArray) - k + 1):
    	sumas.append(sum(inputArray[i:i + k]))
    return max(sumas)
