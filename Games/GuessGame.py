import random

#Promenne
guessTimes = 3
guessWords = ["Tomas", "Peta", "David", "Lucian", "Adam","Martin", "Lukas", "JoJo", "Dan", "Jirka", "Honza"]
guessWord = random.choice(guessWords)
guess = " "

#Hlavni loop
while guessTimes > 0 or guess != guessWord:
    guess = input("Guess the word: ")

    if guess == guessWord:
        print("You guessed the word\nThe secret word is: " + guessWord)
        break
    else:
        print("The word you guessed is wrong!")
        guessTimes -= 1
        print("Number of guesses = " + str(guessTimes))
        
        if guessTimes <= 0:
            print("You lost")
            break
