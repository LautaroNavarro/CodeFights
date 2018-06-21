#By Lautaro Navarro

def digitDegree(n):
    return recursiveFunction(n)

def recursiveFunction(n):
    contador = 0
    if len(str(n)) > 1:
        suma = 0
        contador += 1
        for i in str(n):
            suma += int(i)
        return contador + int ( recursiveFunction(suma))
    else:
        return contador