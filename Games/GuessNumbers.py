import random as rn

randomNumber = rn.randint(1,10)

winCount = 0

def giveClues(number):

    randomClue = rn.randint(0,2)

    if randomClue == 0:
        if number > 5:
            print(f"The number you are guessing is greater than 5")
        else:
            print(f"The number you are guessing is smaller than 5")
    if randomClue == 1:
        if number % 2 == 0:
            print(f"The number you are guessing is even")
        else:
            print("The number you are guessing is odd")
    if randomClue == 2:
        if number % 3 == 0:
            print("The number you are guessing is divideable by 3")




#Main
while True:
    print("Try to guess the number")
    choice = int(input("Your guess: "))

    if choice == randomNumber:
        print(f"You guessed it right\n The number was {randomNumber}")
        winCount +=1
        if winCount == 1:
            print(f"You won {winCount} time")
        else:
            print(f"You won {winCount} times")
        break
    else:
        print("Your guess is wrong!")
        giveClues(randomNumber)
