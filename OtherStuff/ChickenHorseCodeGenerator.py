import random

def generateChickenHorseCode():


    chickenHorseLog = open("ChickenHorseCodeLog.txt","a+")

    lengthOfCode = 4
    chickenHorseCode = ""

    for _ in range(0,lengthOfCode):

        randomLetters = random.choice(["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"])
        chickenHorseCode += randomLetters.upper()

    if chickenHorseCode not in chickenHorseLog.read():
        chickenHorseLog.write(f"{chickenHorseCode}\n")
    else:
        print(f"{chickenHorseCode} DUPLICATE!!!")
        
    chickenHorseLog.close()

    return chickenHorseCode

for _ in range(1000000):
    generateChickenHorseCode()