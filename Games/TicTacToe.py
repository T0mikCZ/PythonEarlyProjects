import random

gameArea = [
    ["N","N","N"],
    ["N","N","N"],
    ["N","N","N"]
]

botDifficulties = ["Easy", "Medium", "Hard"]

def mainMenu():
    print("--MAIN MENU--")
    print("Type 't' to show the tutorial on how to play the game")
    print("1. To play against a dumb bot")
    print("2. To play against another player")
    mainMenuChoice = input("Choose the option: ")

    if(mainMenuChoice == "t"):
        tutorial()
    elif mainMenuChoice == "1":
        chooseDifficulty()
    elif mainMenuChoice == "2":
        play()

def chooseDifficulty():
    print("Bot difficulty:")
    displayBotDifficulties(botDifficulties)

    difficultyChoice = int(input("Choose the difficulty: "))
    play(difficultyHandler(difficultyChoice-1, botDifficulties), True)

def play(difficulty="", playingAgainstBot = False):
    if playingAgainstBot:
        print(f"You are playing against: {difficulty} bot!")
    else:
        print("You are playing against another person!")
    input("Press any key to continue...")
    print("You begin!")
    while True:
        print("\n" + showArea(gameArea) + "\n")
        
        row = int(input("Select row: "))
        column = int(input("Select column: "))

        botChoice = botPlay(gameArea)


        changeValueAtGameList(row, column, gameArea, "X", False)
        print(showArea(gameArea) + "\n")
        playerOneWon = checkWin(gameArea, row, column, "X")
        if playerOneWon:
            resetGameArea(gameArea)
            break
        checkDraw(gameArea)
        if playingAgainstBot:
            changeValueAtGameList(botChoice[0], botChoice[1], gameArea, "O", True)
        else:
            playerTwoRow = int(input("Select row: "))
            playerTwoColumn = int(input("Select column: "))

            changeValueAtGameList(playerTwoRow, playerTwoColumn, gameArea, "O", False)

        playerTwoWon = False
        if playingAgainstBot:
            botHasWon = checkWin(gameArea, botChoice[0], botChoice[1], "O")
        else:
            playerTwoWon = checkWin(gameArea, playerTwoRow, playerTwoColumn, "O")
        if playerOneWon:
            if not playingAgainstBot:
                print(showArea(gameArea) + "\n")
            resetGameArea(gameArea)
            break
        if playingAgainstBot:
            if botHasWon:
                resetGameArea(gameArea)
                break
        if playerTwoWon:
            print(showArea(gameArea) + "\n")
            resetGameArea(gameArea)
            break
        if checkDraw(gameArea): #Draw
            print(showArea(gameArea) + "\n")
            resetGameArea(gameArea)
            break
    if playerOneWon:
        print("Player one has won!")
    elif playerTwoWon:
        print("Player Two has won!")
    elif playingAgainstBot:
        if botHasWon:
            print("Bot have won!")
    else:
        print("Nobody won!. It's a draw")

def tutorial():
    print("The game is played by first typing the row and then the column you want to take")
    print("\nFor example: I'll type 1 to select the first row and 2 to select the second column")

def changeValueAtGameList(row, column, areaList, mark, isBot):
    try:
        if areaList[row-1][column-1] == "N":
            areaList[row-1][column-1] = mark
        elif areaList[row-1][column-1] != "N":
            if isBot:
                botValue = botPlay(areaList)
                changeValueAtGameList(botValue[0], botValue[1], areaList, mark, isBot)
            else:
                print("This point is already taken")
    except IndexError:
        print("Value out of game area!")

def botPlay(gameArea):
    randomRow = random.randint(0, 3)
    randomColumn = random.randint(0, 3)
    return randomRow, randomColumn
    
def displayBotDifficulties(list):
    for i,difficulty in enumerate(list):
        print(f"{i+1}. {difficulty}")

def difficultyHandler(difficulty, list):
    return list[difficulty]

def resetGameArea(gameAreaList):
    for i in range(len(gameAreaList)):
        for j in range(len(gameAreaList)):
            gameAreaList[i][j] = "N"
        
def checkWin(areaList, row, column, letterForWinning):
    row -=1
    column -=1
    try:
        if areaList[row][0] == letterForWinning == areaList[row][1] == areaList[row][2]:
            return True
        if areaList[0][column] == letterForWinning == areaList[1][column] == areaList[2][column]:
            return True
        if row == column and areaList[0][0] == letterForWinning == areaList[1][1] == areaList[2][2]:
            return True
        if row + column == 2 and areaList[0][2] == letterForWinning == areaList[1][1] == areaList[2][0]:
            return True
        return False
    except IndexError:
        print("Value out of game area!")

def checkDraw(areaList):
    for i in range(3):
        for j in range(3):
            if areaList[i][j] == "N":
                return False
    return True

def showArea(areaList):
    modifiedAreaList = str(areaList).replace(", [", "\n").replace("[", "").replace("]", "").replace(",", "").replace("'", "")
    return modifiedAreaList

# Main runtime code

playAgain = "y"

while playAgain == "y".lower():
    
    mainMenu()

    playAgain = input("Do you want to play again? (y/n): ")
