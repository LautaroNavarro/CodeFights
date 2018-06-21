#By Lautaro Navarro

def longestDigitsPrefix(inputString):
    cadena = ""
    for i in inputString:
        if ord(i) >= 48 and ord(i) <= 57:
            cadena += str(i) 
        else:
            break
    return cadena