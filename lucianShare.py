import random

listOfNames = ["Lucian","Tomas","David", "Freeman", "Kleiner"]

randomName = random.choice(listOfNames)

randomChance = random.randint(0,1)
randomPetChance = random.randint(0,5)

print(f"Scientist's name is {randomName}")

if randomName == "Lucian":
    print("You are playing like Scientist Lucian")

    input("Press any key to continue ")

    print("Oh no, you encountered a headcrab. What will you do?")
    print("You have 3 choices")
    print("1. Kill the headcrab")
    print("2. Run away")
    print("3. Pet it")

    playerChoice = input("Choose: ")

    if playerChoice == "1":
        if randomChance == 1:
            print("You killed the headcrab with your barehands")
        else:
            print("Headcrab has jumped on your head and you becamed zombie, game over")
    if playerChoice == "2":
        if randomChance == 1:
            print("You runned, you coward now world is doomed")
        else:
             print("You tried to run but stumbled and fell, even headcrab laughed and then he jumped at your head and you became zombie. You are like walking stereotype, game over")
    if playerChoice == "3":
        if randomPetChance == 5:
            print("You tried to pet the headcrab and it worked he jumped at your head, but he didn't turned you to a zombie. You have now an exotic pet. Congratulations!")
        elif randomPetChance == 3:
            print("When you were chosing, some guy named freeman runned around you and killed headcrab and continued in his way")
        elif randomPetChance == 4:
            print("When you were chosing, headcrab walked away cause he was bored you continued at you path")
        else:
            print("You are really stupid aren't you? Headcrabs are not for petting, headcrab jumped at you and turned you in zombie")