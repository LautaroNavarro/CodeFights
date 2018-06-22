#By Lautaro Navarro

def electionsWinners(votes, k):
    contador = 0
    masGrande = max(votes)
    for i in range(len(votes)):
        if masGrande < votes[i] + k:
            contador += 1
        elif masGrande == votes[i] and votes.count(votes[i]) == 1:
            contador += 1
    return contador