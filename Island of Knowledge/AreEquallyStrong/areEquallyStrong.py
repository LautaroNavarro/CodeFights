#By Lautaro Navarro

def areEquallyStrong(yourLeft, yourRight, friendsLeft, friendsRight):
    if yourLeft > yourRight:
        myStrongArm = yourLeft
        myWeakArm = yourRight
    else:
        myStrongArm = yourRight
        myWeakArm = yourLeft
    if  friendsLeft > friendsRight:
        friendsStrongArm = friendsLeft
        friendWeakArm = friendsRight
    else:
        friendsStrongArm = friendsRight
        friendWeakArm = friendsLeft
    if myStrongArm == friendsStrongArm and myWeakArm == friendWeakArm:
        return True
    else:
        return False