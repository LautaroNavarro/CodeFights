#By Lautaro Navarro

def isBeautifulString(inputString):
    for i in range(97,123):
        letraActual = inputString.count(chr(i))
        print (chr(i),letraActual)
        if i == 97:
            letraAnterior = letraActual
        if  letraAnterior < letraActual:
            return False
        letraAnterior = letraActual
    return True