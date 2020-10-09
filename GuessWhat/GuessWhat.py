from Animal import Animal
import random

wolf = Animal("Wolf", "Mammal", "BARK")
dog = Animal("Dog", "Mammal", "bark")
deer = Animal("Deer", "Mammal", "bellow")
bear = Animal("Bear", "Mammal", "Roar")

animals = [wolf, dog, deer,  bear]
randomAnimal = random.choice(animals)


print("Main Menu")
print("1. Guess Animals")

mainChoice = input("Choose the option: ")

if mainChoice == "1":
    print("You are guessing an animal")
    print(f"The animal is a {randomAnimal.animalClass}")
    print(f"The animal is making a {randomAnimal.animalSound} sound")

    guessChoice = input("Guess the animal: ")

    if guessChoice == randomAnimal.name:
        print("You have guessed the animal")