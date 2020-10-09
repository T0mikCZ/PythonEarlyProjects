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

#Decalring items. It isn't working in a list
phone = Item("Phone", "140g", "Plastic or Metallic", "Any", "Its like a mini computer", True)
keyboard = Item("Keyboard", "540 or >1kg", "Plastic or Metallic", "Usually Black", "Used to smashing keys", True)
chair = Item("Chair", "1kg or more", "Wooden", "Brown or White", "The best thing for a gamer, it can have wheels", False)
fan   = Item("Fan", "1kg or more", "Plastic and Metallic", "Black or White", "Used to cool you down in hot days", True)
car   = Item("Car", "1t or more", "Metallic")

items = [phone, keyboard, chair, fan, car]
randomItem = random.choice(items)
#End of items

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
        print(f"The item weights {randomItem.weight}")
        print(f"The item is {randomItem.material}")
        if randomItem.isElectronic:  
            print("The item is electronic")
        else:
            print("The item isn't")
        print(f"The item has a {randomItem.color} color\n")

        guessChoice = input("Guess the item: ")

        if guessChoice == randomItem.name:
            print(f"You have guessed the item\nThe item was a {randomItem.name}")
            break
        else:
            print("Your guess is wrong/n")  