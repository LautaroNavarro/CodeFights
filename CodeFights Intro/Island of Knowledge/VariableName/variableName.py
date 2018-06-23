#By Lautaro Navarro

def variableName(name):
    if isNotLetter(name[0]) and isNotUnderScore(name[0]):
        return False
    for i in name:
        if isNotLetter(i) and isNotUnderScore(i) and isNotDigit(i):
            return False
    return True

def isNotLetter (i):
        if not(ord(i) >= 65 and ord(i) <= 90 or ord(i) >= 97 and ord(i) <= 122 ):
            return True
def isNotUnderScore(i):
    if  not(ord(i) == 95):
        return True
def isNotDigit(i):
    if  not(ord(i) >= 48 and ord(i) <= 57):
        return True