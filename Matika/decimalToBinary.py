import math

def toBinary(decimalNum):
    bin = ""

    while decimalNum > 1:
        bin += str(int(decimalNum % 2))
        decimalNum /= 2

    if decimalNum == 1:
        bin += "1"
    elif decimalNum <= 0:
        return decimalNum

    return int(bin[::-1])

print(toBinary(56456465465465))


    
        