#By Lautaro Navarro

def isIPv4Address(inputString):
    ipv4 = ['']
    count = 0
    for i in range(len(inputString)):
        if inputString[i] == '.':
            ipv4.append('')
            count += 1
        else:
            ipv4[count] += inputString[i]
    try:
    	if len(ipv4) > 4 or int(ipv4[0]) > 255 or int(ipv4[0]) < 0 or int(ipv4[1]) > 255 or int(ipv4[1]) < 0 or int(ipv4[2]) > 255 or int(ipv4[2]) < 0 or int(ipv4[3]) > 255 or int(ipv4[3]) < 0:
    		return False
    except Exception as e:
    	return False
    return True