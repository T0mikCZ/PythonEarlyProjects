import random as rn

mainChoice = "yes"

while mainChoice == "yes" or mainChoice == "yes".capitalize:
    
    diceRoll = rn.randint(1,6)
    
    input("Press enter")
    print(f"You have rolled {diceRoll}")

    mainChoice = input("Do you want to continue: ")