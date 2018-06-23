#By lautaro Navarro

def bishopAndPawn(bishop, pawn):
    values = {'a' : 0, 'b' : 1 , 'c' : 2 , 'd' : 3, 'e' : 4 , 'f' : 5, 'g' : 6 , 'h' : 7 }
    bishopY = values[bishop[0]]
    bishopX = int(bishop[1]) - 1
    pawnY = values[pawn[0]]
    pawnX = int(pawn[1]) - 1
    contador = 0
    while (True):
        if bishopY + contador == pawnY:
            break
        if bishopY - contador == pawnY:
            break
        contador += 1
    if  pawnX == bishopX + contador or pawnX == bishopX - contador:
        return True
    else:
        return False