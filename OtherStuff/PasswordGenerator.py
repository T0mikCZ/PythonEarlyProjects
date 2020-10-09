import random
import colorama

colorama.init(strip=False)

def makePasswordStronger(password):

    passLog = open("PasswordLog.txt", "a")

    password = str(password)
    password = password.capitalize()
    modPassword = ""

    randomChoice = random.randint(1,2)
    randomSymbol = random.choice(["!","@","#","$","%","&","_",":",":","'","/","~"])
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

    for _ in range(0,lengthOfPassword):

        randomSymbols = random.choice(["!","@","#","$","%","&","_",":",":","'","/","~"])
        randomLetters = random.choice(["A","B","C","D","E","Z","W","B","Y","H","S","O"])
        randomNumber = random.randint(0,9)
        randomChoice = random.randint(1,4)

        if randomChoice == 1:
            password += randomLetters
        elif randomChoice == 2:
            password += randomSymbols
        elif randomChoice == 3:
            password += str(randomNumber)
        else:
            password += randomLetters
            
    passLog.write(f"Password: {password}\n")
    passLog.close()

    return password

print("Main Menu")
print("1. Generate password from a word")
print("2. Random generated password")

passwordMenuChoice = input("Choose generating type: ")

if passwordMenuChoice == "1":

    print("Password Generator from a word!\n")

    inputPassword = input("Type a word you want to strength up: ")

    print(f"Your generated password: {colorama.Fore.CYAN}{makePasswordStronger(inputPassword)}\n{colorama.Style.RESET_ALL}")
    print("Your password has been save to a file: PasswordLog.txt")

elif passwordMenuChoice == "2":
    print("Random password generator!\n")

    passwordLength = int(input("Type a length of the password: "))

    print(f"Your generated password: {colorama.Fore.CYAN}{generatePassword(passwordLength)}\n{colorama.Style.RESET_ALL}")
    print("Your password has been save to a file: PasswordLog.txt")
else:
    print("Choice selected wrongly! You can only select between 1 and 2")


input()
exit()