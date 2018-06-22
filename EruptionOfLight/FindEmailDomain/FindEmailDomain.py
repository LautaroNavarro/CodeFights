#By Lautaro Navarro

def findEmailDomain(address):
    add = address[::-1]
    add = len(address) - add.find("@") - 1
    return address[add  + 1:]