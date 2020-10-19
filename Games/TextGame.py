import random
import json
import time
from GameClass import Job, Food

#def chooseJob(job, jobIndex)

def findJob(jobList, jobIndex):
    currentjob = jobList[jobIndex]
    print(f"You have succesfully got a job as a {currentjob.jobName}")

    config["hasJob"] = True
    config["currentJob"] = currentjob.jobName
    config["jobIndex"] = jobIndex
    configFile =  open("config.json", "w")

    json.dump(config, configFile)

    configFile.close()

def findJobInIfs(jobChoice):

    if jobChoice == "1":

        findJob(jobList, 0)

    elif jobChoice == "2":

        findJob(jobList, 1)

    elif jobChoice == "3":

        findJob(jobList, 2)

    elif jobChoice == "4":

        findJob(jobList, 3)

    elif jobChoice == "5":

        findJob(jobList, 4)
        
    elif jobChoice == "6":

        findJob(jobList, 5)

    elif jobChoice == "7":

        findJob(jobList, 6)                                         

    elif jobChoice == "8":

        findJob(jobList, 7)

    elif jobChoice == "9":

        findJob(jobList, 8)

    else:
        print("The selected choice is wrong!")

#Variables
mainChoice = "yes"

#Create lists
jobList = []
foodList = []
trashFoodList = []
#Add Jobs to list
jobList.append(Job("McDonald's Cook", 25, 5))
jobList.append(Job("Programmer", 40, 10))
jobList.append(Job("Animator", 50, 15))
jobList.append(Job("Construction Worker", 15, 25))
jobList.append(Job("Cook", 35, 20))
jobList.append(Job("Cook in Luxury Restaurant", 45, 25))
jobList.append(Job("Animator", 50, 20))
jobList.append(Job("Cashier", 20, 5))
jobList.append(Job("Politician", 75, 15))
#End of jobs

#Add food to list
foodList.append(Food("Yogurt", 5, 3))
foodList.append(Food("Hamburger", 30, 15))
foodList.append(Food("Kebab", 60, 25))
foodList.append(Food("McDonald small menu", 120, 40))
foodList.append(Food("McDonald big menu", 250, 75))

trashFoodList.append(Food("Spoiled Yogurt", 1, 1))
trashFoodList.append(Food("Half eaten Hamburger", 3, 5))
trashFoodList.append(Food("Smelly Kebab", 5, 10))
trashFoodList.append(Food("Spoiled McDonald small menu", 10, 15))
trashFoodList.append(Food("Spoiled McDonald big menu", 15, 20))
#End of food

jsonFile = open("config.json", "r")
config = json.load(jsonFile)

jobIndex = config["jobIndex"]
currentjob = jobList[jobIndex]

jsonFile.close()

#Main Loop
while mainChoice == "yes" or mainChoice == "yes".capitalize:
    jsonFile = open("config.json", "r")
    config = json.load(jsonFile)

    hasJob = config["hasJob"]
    jobIndex = config["jobIndex"]
    currentConfigJob = jobList[jobIndex]

    print("Main Menu\n")

    print("Food: " + str(config["food"]))
    print("Drink: " + str(config["drink"]))
    print("Health: " + str(config["health"]))
    print("Energy: " + str(config["energy"]))
    print("Money: " + str(config["money"]) + "$" +  "\n")

    energy = config["energy"]
    money = config["money"]

    jsonFile.close()

    if hasJob:
        print("1. Go to work")
    else:
        print("1. Find a job")
    print("2. Go to store")
    print("3. Find a job")
    print("4. Search Trash cans")

    gameChoice = input("Choose an option: ")

    if gameChoice == "1":
        if not hasJob:
            print("You have to find a job!\n")

            for i, job in enumerate(jobList):
                print(f"{i+1}. {job.jobName}")
        
            jobChoice = input("\nChoose a job you want to work at: ")

            findJobInIfs(jobChoice)

        elif hasJob:
            def work(jobList, hoursToWork):
                energy = config["energy"]

                print(f"You have {energy} energy!")

                if hoursToWork <= 8 and hoursToWork > 0:
                    job = jobList[jobIndex]
                    if energy < 0 or (job.jobEnergy * hoursToWork) > energy:

                        print("You don't have enough energy to work this many hours!")

                    else:

                        print(f"You are employed as a {job.jobName}")

                        input("If you want to work, then press any key: ")

                        print("You work...")
                        time.sleep(hoursToWork)

                        print(f"You have worked for {hoursToWork} hours")
                        print(f"You have earned {job.jobSalary * hoursToWork}$")

                        config["money"] += job.jobSalary * hoursToWork
                        config["energy"] -= job.jobEnergy * hoursToWork
                        config["food"] -= int((job.jobEnergy * hoursToWork) / 3)
                        config["drink"] -= int((job.jobEnergy * hoursToWork) / 2)
                        configFile =  open("config.json", "w")
                        json.dump(config, configFile)

                        configFile.close()

                else:
                    print("The number of hours has to be less than 9 and more than 0 hours you slaver")

            workChoice = "yes"
            while workChoice == "yes" or workChoice == "yes".capitalize:
                hoursToWork = int(input("How many hours do you want to work: "))

                work(jobList, hoursToWork)

                workChoice = input("Do you want to work more?: ")
    elif gameChoice == "2":
        def buy(itemList, itemIndex):
            food = itemList[itemIndex]
            money = config["money"]

            if food.cost > money or money <= 0:
                print(f"The food: {food.name}, you want to buy is too expensive\nYou have {money}$")
            else:
                if food.name == "McDonald big menu" or food.name == "McDonald small menu":
                    print(f"You have bought and ate {food.name}")

                    config["money"] -= food.cost
                    config["energy"] += food.bonus
                    config["food"] += food.bonus
                    config["drink"] += food.bonus

                    configFile =  open("config.json", "w")
                    json.dump(config, configFile)

                    configFile.close()
                else:
                    print(f"You have bought and ate {food.name}")

                    config["money"] -= food.cost
                    config["energy"] += food.bonus
                    config["food"] += food.bonus

                    configFile =  open("config.json", "w")
                    json.dump(config, configFile)

                    configFile.close()

        storeBuyFoodChoice = "yes"
        while storeBuyFoodChoice == "yes" or storeBuyFoodChoice == "yes".capitalize:
            print("\nYou are in store!\n")

            for i, item in enumerate(foodList):
                print(f"{i+1}. {item.name}, costs: {item.cost}$")
            foodIndex = int(input("What do you want to buy? Input a nubmer of the item: "))
            foodIndex -= 1

            buy(foodList, foodIndex)

            storeBuyFoodChoice = input("Do you want to buy more food?: ")
    elif gameChoice == "3":
        if hasJob:
            hasJob = False

            print("You are changing your job!\n")
            for i, job in enumerate(jobList):
                print(f"{i+1}. {job.jobName}")
        
            jobChoice = input("\nChoose a job you want to work at: ")

            findJobInIfs(jobChoice)
        else:
            print("You can't change a job when you haven't got any job :D")
    elif gameChoice == "4":
        def search(itemList, itemIndex):
            food = itemList[itemIndex]


            if food.name == "McDonald big menu" or food.name == "McDonald small menu":
                print(f"You have searched and ate {food.name}")

                config["health"] -= food.cost
                config["energy"] += food.bonus
                config["food"] += food.bonus
                config["drink"] += food.bonus

                configFile =  open("config.json", "w")
                json.dump(config, configFile)

                configFile.close()
            else:
                print(f"You have searched and ate {food.name}")

                config["health"] -= food.cost
                config["energy"] += food.bonus
                config["food"] += food.bonus

                configFile =  open("config.json", "w")
                json.dump(config, configFile)

                configFile.close()

        randomTrash = random.randint(1,2)
        specialTrash = random.randint(1,2)
        randomIndex = random.randint(0, len(trashFoodList))

        print("You are searching trash cans!")

        if randomTrash == 1:
            print("You have found nothing!")
        else:
            if specialTrash == 1:
                print("You have found nothing!")
            else:
                search(trashFoodList, randomIndex)

    mainChoice = input("Do you want to return to main menu?: ")

 