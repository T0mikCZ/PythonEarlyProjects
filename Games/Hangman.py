import random as rn

randomName = rn.choice(["Kokot", "Martin", "Gay", "Programator"])

numberOfGuesses = 3

while True:
    guessWord = ""
    print("You play Hangman \nGuess the word\n")

    guessChar = input("Type a charcter: ")

    if guessChar in randomName and guessWord != randomName:
        guessWord += guessChar
        print(f"The character {guessChar}, you have typed is right\n")
    else:
        numberOfGuesses -= 1
        print(f"The character {guessChar}, you have typed is wrong\n")

