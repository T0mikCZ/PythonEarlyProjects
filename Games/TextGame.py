import random
import json


while True:
    jsonFile = open("C:\Python\Games\config.json", "r")
    config = json.load(jsonFile)

    print("Main Menu")

    print("Food: " + str(config["food"]))
    print("Drink: " + str(config["drink"]))
    print("Health: " + str(config["health"]))
    print("Energy: " + str(config["energy"]) + "\n")

    jsonFile.close()


