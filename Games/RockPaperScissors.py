import random

playersName = input("Type you name: ")

numberOfRounds = int(input("How many times do you want to play: "))

mainChoice = "yes"

#Main function for the game to work
def play(name, repeatTimes):
    #Variables of the game
    rock = "R"
    paper = "P"
    scissors = "S"

    playerWinCount = 0
    botWinCount = 0

    #Check so its doesn't break the game
    if repeatTimes <=0:
        print("The number of times you want to play has to be greater than 0")
        input()
        exit()

    print("You are playing: rock, paper, scissors!")

    while repeatTimes > 0:

        randomChoice = random.choice(["R", "P", "S"])

        choice = input("Choose R,P,S: ")

        if choice == rock:
            if randomChoice == paper:
                repeatTimes -= 1
                botWinCount += 1 

                print(f"The bot's choice was {randomChoice}")
                print("The bot has won the round!")
            elif randomChoice == rock:
                repeatTimes -= 1

                print(f"The bot's choice was {randomChoice}")
                print(f"Its a tie!")
            else:
                repeatTimes -= 1
                playerWinCount += 1 

                print(f"The bot's choice was {randomChoice}")
                print(f"The player {name} has won the round!")
        elif choice == paper:
            if randomChoice == scissors:
                repeatTimes -= 1
                botWinCount += 1

                print(f"The bot's choice was {randomChoice}") 
                print("The bot has won the round!")
            elif randomChoice == paper:
                repeatTimes -= 1

                print(f"The bot's choice was {randomChoice}")
                print(f"Its a tie!")
            else:
                repeatTimes -= 1
                playerWinCount += 1 

                print(f"The bot's choice was {randomChoice}")
                print(f"The player {name} won the round!")    
        elif choice == scissors:
            if randomChoice == rock:
                repeatTimes -= 1
                botWinCount += 1 

                print(f"The bot's choice was {randomChoice}")
                print("the bot has won the round!")
            elif randomChoice == scissors:
                repeatTimes -= 1

                print(f"The bot's choice was {randomChoice}")
                print(f"Its a tie!")
            else:
                repeatTimes -= 1
                playerWinCount += 1 
                
                print(f"The bot's choice was {randomChoice}")
                print(f"The player {name} has won the round!")
        else:
            print("You have chosen the wrong answer. You have to type R,S or P")

        if repeatTimes == 0:
            if playerWinCount > botWinCount:
                print(f"\nThe player {name} has won the game!")
                print(f"\nThe {name}'s score is {playerWinCount} while the bot's score was {botWinCount}")
                break
            elif playerWinCount == botWinCount:
                print("\nNo body wins! Its a tie")
                print(f"The {name}'s score is {playerWinCount} while the bot's score was {botWinCount}")
                break
            else:
                print("\nThe bot has won the game!")
                print(f"The {name}'s score is {playerWinCount} while the bot's score was {botWinCount}")
                break

#While loop to repeat the game
while mainChoice == "yes" or mainChoice == "yes".capitalize:
    play(playersName, numberOfRounds)

    mainChoice = input("Do you want to play again?: ")