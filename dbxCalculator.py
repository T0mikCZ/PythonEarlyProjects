#Funkce
def calculateExps(rebirths, eventMultipliler):

    result = 0.2 * rebirth + 1.0

    if(eventMultipliler == 0 or None):
        return result
    else:
        return result * eventMultipliler



def nextRebirthExp(rebirths):

    return 3000000 * rebirth - 1000000

#Main
rebirth = int(input("Enter the number of rebirths: "))

multiplier = int(input("Enter a exp event multiplier you can leave it to 0 if there is no xp event: "))

print("Requierments for the next rebirth: " +  str(nextRebirthExp(rebirth)))

print("Exp multiplier: " + str(calculateExps(rebirth, multiplier)))

input()