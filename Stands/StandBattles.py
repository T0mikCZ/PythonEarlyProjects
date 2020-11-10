from playsound import playsound
import random
from Stand import Stand, GoldExperience, TheWorld

goldExperience = GoldExperience("Gold Experience", "C", "A", "C", "C", "A", 100)
starPlatinum = Stand("Star Platinium", "A", "A", "C", "A", "C", 100)
theWorld = TheWorld("The World", "A", "A", "C", "B", "B", 100)
killerQueen = Stand("Killer Queen", "A", "B", "D", "B", "A", 100)

goldExperience.Heal()
goldExperience.Barrage("Mudaa")
theWorld.ThrowKnife(goldExperience)
goldExperience.Heal()

stands = [goldExperience, starPlatinum, theWorld, killerQueen]

choice = input("Welcome to a Fighting Text Game !!! CHOOSE A CHARACTER : ")

Char = ["Giorno Giovanna", "Jotaro Kujo" , "Goku", "Dio Brando", "Vegeta", "Kira Yoshikage"]
randomEnemy = random.choice (Char)
if choice in Char:
    print(f"you will fight {randomEnemy}")