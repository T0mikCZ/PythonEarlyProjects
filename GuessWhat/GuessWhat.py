from Animal import Animal
from Item import Item
import random

#Decalring animals. It isn't working in a list
wolf = Animal("Wolf", "Mammal", "BARK", "Grey or white",True)
dog = Animal("Dog", "Mammal", "Bark", "Usually brown", True)
deer = Animal("Deer", "Mammal", "Bellow", "Brown", True)
bear = Animal("Bear", "Mammal", "Roar", "Brown", True)
guineaPig = Animal("Guinea Pig", "Rodent", "Squeeks", "Usually grey", True)
pig = Animal("Pig", "Mammal", "Snort", "Pink", False)
frog = Animal("Frog", "Amphibian", "Croak", "Usually green", False)
ape = Animal("Ape", "Mammal", "Gibber", "Usually black or brown", True)
turtle = Animal("Turtle", "Amphibian", "Hissing", "Green", False)
snake = Animal("Snake", "Amphibian", "Shriek", "Green", False)
dio = Animal("Dio", "Mammal", "Wryyyyy!", "Yellow", False)

animals = [wolf, dog, deer, bear, guineaPig, pig, frog, ape, turtle, snake, dio]
randomAnimal = random.choice(animals)
#End of animals

phone = Item("Phone", 140, "Plastic or Metallic", "Any color")

items = [phone]
randomItem = random.choice(items)


print("Main Menu")
print("1. Guess Animals")
print("2. Guess Items")

mainChoice = input("Choose the option: ")


while True:

    if mainChoice == "1":
        print("You are guessing an animal\n")
        print(f"The animal is a {randomAnimal.animalClass}")
        print(f"The animal is {randomAnimal.color}")
        if randomAnimal.hasCoat:  
            print("The animal has a coat")
        else:
            print("the animal hasn't got a coat")
        print(f"The animal is making a {randomAnimal.animalSound} sound\n")

        guessChoice = input("Guess the animal: ")

        if guessChoice == randomAnimal.name:
            print(f"You have guessed the animal\nThe animal was a {randomAnimal.name}")
            break
        else:
            print("Your guess is wrong/n")  
    elif mainChoice == "2":
        print("You are guessing an item\n")
        print(f"The item is a {randomAnimal.animalClass}")
        print(f"The animal is {randomAnimal.color}")
        if randomAnimal.hasCoat:  
            print("The animal has a coat")
        else:
            print("the animal hasn't got a coat")
        print(f"The animal is making a {randomAnimal.animalSound} sound\n")

        guessChoice = input("Guess the animal: ")

        if guessChoice == randomAnimal.name:
            print(f"You have guessed the animal\nThe animal was a {randomAnimal.name}")
            break
        else:
            print("Your guess is wrong/n")  