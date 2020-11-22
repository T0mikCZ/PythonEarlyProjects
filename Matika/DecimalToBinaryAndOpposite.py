import math

def decimalToBinary(cislo):
    binaryList = []

    while cislo > 1:
        binaryList.append(math.floor(cislo%2))
        cislo /= 2

    binaryList.reverse()
    convertedBinaryInt = int("".join(map(str, binaryList)))

    return convertedBinaryInt

def binaryToDecimal(binaryCislo):
    powNumber = len(str(binaryCislo))
    desitkoveCislo = 0

    for i in range(len(str(binaryCislo))):
        cisloNaIndexu = str(binaryCislo)[i]
        desitkoveCislo = 2 * desitkoveCislo + int(cisloNaIndexu)
        powNumber -= 1
        
    return desitkoveCislo

print(decimalToBinary(4563456))
print(binaryToDecimal(10001011010001000000000))