import random
import json
import time
from JobClass import Job

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
#Variables
mainChoice = "yes"

#Create job list
jobList = []
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
    currentConfigJob = config["currentJob"]

    print("Main Menu\n")

    print("Food: " + str(config["food"]))
    print("Drink: " + str(config["drink"]))
    print("Health: " + str(config["health"]))
    print("Energy: " + str(config["energy"]))
    print("Money: " + str(config["money"]) + "$" +  "\n")

    energy = config["energy"]

    jsonFile.close()

    if hasJob:
        print("1. Go to work")
    else:
        print("1. Find a job")
    print("2. Go to store")

    gameChoice = input("Choose an option: ")

    if gameChoice == "1":
        if not hasJob:
            print("You have to find a job!\n")
            for i, job in enumerate(jobList):
                print(f"{i+1}. {job.jobName}")
            
            jobChoice = input("\nChoose a job you want to work at: ")

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
        elif hasJob:
            def work(jobList, hoursToWork):
                energy = config["energy"]

                print(f"You have {energy} energy!")

                if hoursToWork < 8 and hoursToWork > 0:
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
                        configFile =  open("config.json", "w")
                        json.dump(config, configFile)

                        configFile.close()

                else:
                    print("The number of hours has to be less than 8 and more than 0 hours you slaver")

            workChoice = "yes"
            while workChoice == "yes" or workChoice == "yes".capitalize:
                hoursToWork = int(input("How many hours do you want to work: "))

                work(jobList, hoursToWork)

                workChoice = input("Do you want to work more?: ")
    mainChoice = input("Do you want to return to main menu?: ")

 