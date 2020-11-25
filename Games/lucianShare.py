import random

listOfNames = ["Lucian","Tomas","David", "Freeman", "Kleiner"]
weaponList = []

randomName = random.choice(listOfNames)

randomChance = random.randint(0,1)
randomPetChance = random.randint(0,5)

def findWeaponInList(weaponName):
    for weapon in weaponList:
        if weapon == weaponName:
            return weapon
        else:
            return -1

def locateWeapon(weaponName):
    print(f"You have found a {weaponName}!")
    print("You have 2 choices")
    print("1. Pick it up")
    print("2. Leave it on ground")

    pickWeaponChoice = input("Choose now: ")
    if pickWeaponChoice == "1":
        print(f"You have picked the {weaponName}!")
        weaponList.append(weaponName)
    else:
        print("You have left the gun on the ground, WOW")

def headCrabEncounter(name):
    print("Oh no, you encountered a headcrab. What will you do?")
    print("You have 3 choices")
    print("1. Kill the headcrab")
    print("2. Run away")
    print("3. Pet it")

    headCrabChoice = input("What will you do?: ")
    if headCrabChoice == "1":
        if randomChance == 1:
            print("You killed the headcrab with your barehands")
            return 1
        else:
            print("The headcrab has jumped on your head and killed you")
    elif headCrabChoice == "2":
        if randomChance == 1:
            print("You runned away. The world is doomed")
        else:
            print("You tried to run away, but you stumbled and fell on your head. You are dead")
    elif headCrabChoice == "3":
        if randomPetChance == 5:
            print("You tried to pet the headcrab and it worked he jumped at your head, but he didn't turned you to a zombie. You have now an exotic pet. Congratulations!")
        elif randomPetChance == 3:
            print("When you were chosing, some guy named freeman runned around you and killed headcrab and continued in his way")
        elif randomPetChance == 4:
            print("When you were chosing, headcrab walked away cause he was bored you continued at you path")
        else:
            print("You are really stupid aren't you? Headcrabs are not for petting, headcrab jumped at you and turned you in to a zombie")

def zombieEncounter(name):
    print("You have encountered a zombie")
    print("You have 3 choices")
    if findWeaponInList("Pistol"):
        print("1. Kill it with pistol")
    else:
        print("1. Try to kill it with barehands")
    print("2. Run away")
    print("3. Try to pet it")
    
    zombieChoice = input("What will you do?: ")

def vortignautEncounter():
    print("You have encountered a Vortignaut. What will you do?")
    print("You have 5 choices")
    print("1. Kill the Vortignaut")
    print("2. Reference")
    print("3. Invite Mr.Vortignaut for a beer")
    print("4. Nigerundayooo!!!")
    print("5. ???hfdshffn:?:!!§ů¨ß$ß$[&]")

    playerVortignautChoice = input("Choose: ")
    if playerVortignautChoice == "1":
        print("You killed Vortignaut")
    if playerVortignautChoice == "2":
        print("You said 'Hoooooo so you are approching me kono DIO!'Vortignaut shooted lightning bolt from his hands and killed you did you really think this will work ? ")
    if playerVortignautChoice == "3":
        print("You tried to invite Mr.Vortignaut to a beer but he killed you")
    else: 
        print("You invited Mr.Vortignaut to a beer and he accepted")
    if playerVortignautChoice == "4":
        print("You runned away and screaming NIGERUNDAYOOOO!!!")
    if playerVortignautChoice == "5":
        print("You stopped time and muda barraged Vortignaut")
    else: 
        print("You trird to stop time but you only farted and Vortignaut killed you")    


if randomName == "Lucian":
    print("You are playing like Scientist Lucian")
    input("Press any key to continue ")

    headCrabEncounter(randomName)

    if headCrabEncounter(randomName):
        locateWeapon("Pistol")
exit()