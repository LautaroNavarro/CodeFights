# By Lautaro Navarro

def alternatingSums(a):
    teams = [0,0]
    for i in range (len(a)):
        if i == 0:
            teams[0] += a[i]
        elif i  % 2 == 0:
            teams[0] += a[i]
        else:
            teams[1] += a[i]
    return teams