import random
import colorama

colorama.init(strip=False)

def generatePassword(password):
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

print("Password Generator!\n")

inputPassword = input("Type a word you want to strength up: ")

print(f"Your generated password: {colorama.Fore.CYAN}{generatePassword(inputPassword)}\n{colorama.Style.RESET_ALL}")
print("Your password has been save to a file: PasswordLog.txt")

input()
exit()