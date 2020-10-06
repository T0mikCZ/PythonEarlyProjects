import random

listOfNames = ["Lucian","Tomas","David", "Freeman", "Kleiner"]

randomName = random.choice(listOfNames)

randomChance = random.randint(0,1)
randomPetChance = random.randint(0,5)
hasPistol = False

print(f"Scientist's name is {randomName}")

if randomName == "Lucian":
    print("You are playing like Scientist Lucian")

    input("Press any key to continue ")

    print("Oh no, you encountered a headcrab. What will you do?")
    print("You have 3 choices")
    print("1. Kill the headcrab")
    print("2. Run away")
    print("3. Pet it")

    playerMainChoice = input("Choose: ")

    if playerMainChoice == "1":
        if randomChance == 1:

            zombiePetChance = random.randint(0,5)
            
            print("You killed the headcrab with your barehands")
            input("Press anything to continue: ")
            print("You have found a pistol")
            print("You have 2 choices")
            print("1. Pick it up")
            print("2. Leave it alone")

            choice = input("Choose: ")

            if choice == "1":
                print("You picked up pistol!")
                hasPistol = True 
            elif choice == "2":
                print("You left pistol on ground everyone is disappointed")

            print("Oh no, you have encountered a zombie!")
            print("What will you do?")
            print("1. Run away")
            if hasPistol:
                print("2. Kill it with pistol")
            else:
                print("2. Try to kill it with barehands")
            print("3. Offer him a donut")

            zombieChoice = input("Choose: ")

            if zombieChoice == "1":
                if randomChance == 1:
                    print(" You succesfully runned away, coward")
                else:
                    print("You tried to run but you runned straight to the zombie and he eated you")
            elif zombieChoice == "2":
                if hasPistol:
                    print("You shoot zombie in the head")  
                else:
                    if randomChance == 1:
                        print("You tried to kill him with your barehands but he only laughed and bite your hands then he eated your brain")
                    else:
                        print("You succesfully killed him with you barehands, you are really crazy")
            elif zombieChoice == "3":
                if zombiePetChance == 5:
                    print("You gived zombie a donut he eat it and leaved you alone")
                else:
                    print("You really think you can make a zombie friend you are really a fool, zombie almost eat your arm then he killed you")
                    
            
        else:
            print("Headcrab has jumped on your head and you becamed zombie, game over")
    if playerMainChoice == "2":
        if randomChance == 1:
            print("You runned, you coward now world is doomed")
        else:
             print("You tried to run but stumbled and fell, even headcrab laughed and then he jumped at your head and you became zombie. You are like walking stereotype, game over")
    if playerMainChoice == "3":
        if randomPetChance == 5:
            print("You tried to pet the headcrab and it worked he jumped at your head, but he didn't turned you to a zombie. You have now an exotic pet. Congratulations!")
        elif randomPetChance == 3:
            print("When you were chosing, some guy named freeman runned around you and killed headcrab and continued in his way")
        elif randomPetChance == 4:
            print("When you were chosing, headcrab walked away cause he was bored you continued at you path")
        else:
            print("You are really stupid aren't you? Headcrabs are not for petting, headcrab jumped at you and turned you in zombie")


exit()