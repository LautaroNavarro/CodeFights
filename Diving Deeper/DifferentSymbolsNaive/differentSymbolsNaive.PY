#By Lautaro Navarro

def differentSymbolsNaive(s):
    chars = {}
    for i in s:
        if  not i in chars:
            chars[i] = 1
    return len(chars)