import random as rn

winCount = 0
hasWon = False

randomNumber = rn.randint(1,100)

#Function that generates random clues to the player
def giveClues(number):

    randomClue = rn.randint(0,3)

    if randomClue == 0:
        if number > 50:
            print(f"The number you are guessing is greater than 50")
        else:
            print(f"The number you are guessing is smaller than 50")
    if randomClue == 1:
        if number % 2 == 0:
            print(f"The number you are guessing is even")
        else:
            print("The number you are guessing is odd")
    if randomClue == 2:
        if number % 3 == 0:
            print("The number you are guessing is divideable by 3")
        elif number % 5 == 0:
            print("The number you are guessing is divideable by 5")
        elif number % 5 == 0 and number % 3 == 0:
            print("The number you are guessing is divideable by 5 and 3")
    if randomClue == 3:
        if number >= 10 and number <= 99:
            print("The number has 2 digits")
        elif number >= 100:
            print("The number has 3 digits")
        else:
            print("The number has 1 digit")

#Main
while True:

    print("Try to guess the number\n")
    choice = int(input("Your guess: "))

    if choice == randomNumber:
        print(f"You guessed it right\n The number was {randomNumber}")
        winCount +=1
        hasWon = True
        if winCount == 1:
            print(f"You won {winCount} time")
        else:
            print(f"You won {winCount} times")
        break
    else:
        print("Your guess is wrong!\n")
        giveClues(randomNumber)