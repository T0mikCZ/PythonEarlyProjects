import random

gameArea = [
    ["N","N","N"],
    ["N","N","N"],
    ["N","N","N"]
]

botDifficulties = ["Easy", "Medium", "Hard"]

hasWon = False

def mainMenu():
    print("--MAIN MENU--")
    print("Type 't' to show the tutorial on how to play the game")
    mainMenuChoice = input("Press any key to play...")

    if(mainMenuChoice == "t"):
        tutorial()
    else:
        chooseDifficulty()

def chooseDifficulty():
    print("Bot difficulty:")
    botDifficultyList(botDifficulties)

    difficultyChoice = int(input("Choose the difficulty: "))
    play(difficultyHandler(difficultyChoice-1, botDifficulties))

def play(difficulty):
    print(f"You are playing against: {difficulty} bot!")
    print("\nYou begin!\n")

    playerChoice = ""

    while playerChoice != "n":
        print(showArea(gameArea))

        row = int(input("Select row: "))
        column = int(input("Select column: "))


        changeValueAtGameList(row, column, gameArea)
        print(showArea(gameArea))
        checkWin(gameArea, "X")
        if checkWin(gameArea, "X"):
            break
        playerChoice = input("Continue?... ")

    if checkWin:
        print("You have won!")

def tutorial():
    print("The game is played by typing the game area number, so that you can take the point you wanted to take")
    print("\nFor example: I'll type 1 to select the first row ad 2 to select the second column")

def changeValueAtGameList(row, column, areaList):
    if areaList[row-1][column-1] == "N":
        areaList[row-1][column-1] = "X"
    else:
        print("This point is already taken")

def botPlay(gameArea):
    randomRow = random.randint(0, 3)
    randomColumn = random.randint(0, 3)
    
def botDifficultyList(list):
    for i,difficulty in enumerate(list):
        print(f"{i+1}. {difficulty}")

def difficultyHandler(difficulty, list):
    return list[difficulty]

def checkWin(areaList, letterforChecking):
    global amountOfTaken
    amountOfTaken = 0
    for i in range(3):
        if areaList[0][i] == letterforChecking:
            amountOfTaken += 1
            if amountOfTaken == 3:
                return True
            elif i == 2:
                amountOfTaken = 0

def showArea(areaList):
    modifiedAreaList = str(areaList).replace(", [", "\n").replace("[", "").replace("]", "").replace(",", "").replace("'", "")
    return modifiedAreaList

# Main runtime code

playAgain = "y"

while playAgain == "y".lower():
    
    mainMenu()

    playAgain = input("Do you want to play again? (y/n): ")
