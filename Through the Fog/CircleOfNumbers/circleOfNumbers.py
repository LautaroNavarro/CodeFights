#By Lautaro Navarro

def circleOfNumbers(n, firstNumber):
    if firstNumber < (n / 2) :
        return ((n + firstNumber * 2)/2)
    else:
        return (firstNumber - (n - firstNumber))/2