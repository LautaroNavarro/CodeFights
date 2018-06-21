#By Lautaro Navarro

def growingPlant(upSpeed, downSpeed, desiredHeight):
    contador = 0
    altura = 0
    while(altura < desiredHeight):
        contador += 1
        altura += upSpeed
        if altura >= desiredHeight:
            break
        else:
            altura -= downSpeed
    return contador