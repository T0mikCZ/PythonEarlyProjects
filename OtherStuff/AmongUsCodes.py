import random

def generateAmongUsCode():


    amongUsLog = open("AmongUsCodeLog.txt","a+")

    lengthOfCode = 5
    amongUsCode = ""

    for _ in range(0,lengthOfCode):

        randomLetters = random.choice(["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"])
        amongUsCode += randomLetters.upper()
        
    finalAmongUsCode = amongUsCode + "Q"

    if finalAmongUsCode not in amongUsLog.read():
        amongUsLog.write(f"{finalAmongUsCode}\n")
    else:
        print(f"{finalAmongUsCode} DUPLICATE!!!")
        
    amongUsLog.close()

    return finalAmongUsCode

for _ in range(1000000):
    generateAmongUsCode()