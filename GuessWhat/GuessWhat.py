from Animal import Animal
import random

wolf = Animal("Wolf", "Mammal", "BARK")
dog = Animal("Dog", "Mammal", "bark")
deer = Animal("Deer", "Mammal", "bellow")
bear = Animal("Bear", "Mammal", "Roar")
guineaPig = Animal("Guinea Pig", "Rodent", "squiks")
pig = Animal("Pig", "Mammal", "Snort")

animals = [wolf, dog, deer,  bear]
randomAnimal = random.choice(animals)


print("Main Menu")
print("1. Guess Animals")

mainChoice = input("Choose the option: ")

print("You are guessing an animal\n")

while True:

    if mainChoice == "1":
        print(f"The animal is a {randomAnimal.animalClass}")
        print(f"The animal is making a {randomAnimal.animalSound} sound\n")

        guessChoice = input("Guess the animal: ")

        if guessChoice == randomAnimal.name:
            print(f"You have guessed the animal\nThe animal was a {randomAnimal.name}")
            break
        else:
            print("Your guess is wrong/n")  