import random
import colorama
import time

colorama.init(strip=False)


def makePasswordStronger(password):

    passLog = open("PasswordLog.txt", "a")

    password = str(password)
    password = password.capitalize()
    modPassword = ""

    randomChoice = random.randint(1,2)
    randomSymbol = random.choice(["!","@","#","$","%","&","_",":",";","'","/","~","?",",","."])
    randomPassNumber = random.randint(100,10000)

    if randomPassNumber == 123 or randomPassNumber == 1234 or randomPassNumber == 12345:
        randomPassNumber += random.randint(1,9) + 2

    for i in range(0,len(password)):
        if randomChoice == 1: 
            if i % 2 == 0:
                modPassword += password[i].upper()
            else:
                modPassword += password[i] 
        else:
            if i % 2 == 0:
                modPassword += password[i].lower()
            else:
                modPassword += password[i].upper()


    finalPassword = randomSymbol + modPassword + randomSymbol + f"{randomPassNumber}" + randomSymbol

    passLog.write(f"Password: {finalPassword}\n")
    passLog.close()

    return finalPassword

def generatePassword(lengthOfPassword):

    passLog = open("PasswordLog.txt","a")

    password = ""

    if lengthOfPassword > 100 and lengthOfPassword < 1000:
        print("Do you really want to have that large password? XD: ")
        input
    elif lengthOfPassword > 1000 and lengthOfPassword < 100000:
        print("Are you fking kidding me with that length? ")
        input()
    elif lengthOfPassword > 1000000:
        print("This is the last time i'm executing something that large")
        input()
    for _ in range(0,lengthOfPassword):

        randomSymbols = random.choice(["!","@","#","$","%","&","_",":",";","'","/","~","?",",","."])
        randomLetters = random.choice(["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"])
        randomNumber = random.randint(0,9)
        randomChoice = random.randint(1,4)

        if randomChoice == 1:
            password += randomLetters
        elif randomChoice == 2:
            password += randomSymbols
        elif randomChoice == 3:
            password += str(randomNumber)
        else:
            password += randomLetters.upper()
            
    passLog.write(f"Password: {password}\n")
    passLog.close()

    return password

def displayPasswordsFromFile(fileName):
    passFile = open(f"{fileName}.txt", "r")
    passwords = passFile.readlines()

    for i,line in enumerate(passwords):
        print(f"{colorama.Fore.CYAN}{i+1}.{line.strip()}{colorama.Style.RESET_ALL}")
        
    passFile.close()

print("Main Menu")
print("1. Generate password from a word")
print("2. Random generated password")
print("3. Displays all saved passwords")

passwordMenuChoice = input("Choose a generating type: ")

startTime = time.time()

if passwordMenuChoice == "1":
    print("Password Generator from a word!\n")

    inputPassword = input("Type a word you want to strength up: ")

    startTime = time.time()

    print(f"Your generated password: {colorama.Fore.CYAN}{makePasswordStronger(inputPassword)}\n{colorama.Style.RESET_ALL}")
    print("Your password has been saved to a file: PasswordLog.txt")

elif passwordMenuChoice == "2":
    print("Random password generator!\n")

    passwordLength = int(input("Type a length of the password: "))

    startTime = time.time()

    print(f"Your generated password: {colorama.Fore.CYAN}{generatePassword(passwordLength)}\n{colorama.Style.RESET_ALL}")
    print("Your password has been saved to a file: PasswordLog.txt")
elif passwordMenuChoice == "3":
    print("Password Display!\n")

    startTime = time.time()

    displayPasswordsFromFile("PasswordLog")

else:
    print("Choice selected wrongly! You can only select between 1 and 3")

executionTime = (time.time() - startTime)

print(f"The time it took to execute the code: {colorama.Fore.RED}{executionTime}{colorama.Style.RESET_ALL}")

input()
exit()