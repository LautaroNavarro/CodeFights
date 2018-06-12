#By Lautaro Navarro

def depositProfit(deposit, rate, threshold):
    contador = 0
    while (deposit < threshold):
        deposit += (rate * deposit) / 100
        contador += 1
    return contador