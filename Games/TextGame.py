import random
import json
import time
from JobClass import Job

#def chooseJob(job, jobIndex, )


#Variables
mainChoice = "yes"

#Create job list
jobList = []
#Add Jobs to list
jobList.append(Job("McDonald's Cook", 25))
jobList.append(Job("Programmer", 40))
jobList.append(Job("Animator", 50))
jobList.append(Job("Construction Worker", 15))
jobList.append(Job("Cook", 35))
jobList.append(Job("Cook in Luxury Restaurant", 45))
jobList.append(Job("Animator", 50))
jobList.append(Job("Cashier", 20))
jobList.append(Job("Politician", 75))
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

    jsonFile.close()

    if hasJob:
        print("1. Got to work")
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
                currentjob = jobList[0]
                print(f"You have succesfully got a job as a {currentjob.jobName}")

                config["hasJob"] = True
                config["currentJob"] = currentjob.jobName
                config["jobIndex"] = 0
                configFile =  open("config.json", "w")

                json.dump(config, configFile)

                configFile.close()

            elif jobChoice == "2":
                currentjob = jobList[1]
                print(f"You have succesfully got a job as a {currentjob.jobName}")

                config["hasJob"] = True
                config["currentJob"] = currentjob.jobName
                config["jobIndex"] = 1
                configFile =  open("config.json", "w")

                json.dump(config, configFile)

                configFile.close()

            elif jobChoice == "3":
                currentjob = jobList[2]
                print(f"You have succesfully got a job as a {currentjob.jobName}")

                config["hasJob"] = True
                config["currentJob"] = currentjob.jobName
                config["jobIndex"] = 2
                configFile =  open("config.json", "w")

                json.dump(config, configFile)

                configFile.close()

            elif jobChoice == "4":
                currentjob = jobList[3]
                print(f"You have succesfully got a job as a {currentjob.jobName}")

                config["hasJob"] = True
                config["currentJob"] = currentjob.jobName
                config["jobIndex"] = 3
                configFile =  open("config.json", "w")

                json.dump(config, configFile)

                configFile.close()

            elif jobChoice == "5":
                currentjob = jobList[4]
                print(f"You have succesfully got a job as a {currentjob.jobName}")

                config["hasJob"] = True
                config["currentJob"] = currentjob.jobName
                config["jobIndex"] = 4
                configFile =  open("config.json", "w")

                json.dump(config, configFile)

                configFile.close()
                
            elif jobChoice == "6":
                currentjob = jobList[5]
                print(f"You have succesfully got a job as a {currentjob.jobName}")

                config["hasJob"] = True
                config["currentJob"] = currentjob.jobName
                config["jobIndex"] = 5
                configFile =  open("config.json", "w")

                json.dump(config, configFile)

                configFile.close()    

            elif jobChoice == "7":
                currentjob = jobList[6]
                print(f"You have succesfully got a job as a {currentjob.jobName}")

                config["hasJob"] = True
                config["currentJob"] = currentjob.jobName
                config["jobIndex"] = 6
                configFile =  open("config.json", "w")

                json.dump(config, configFile)

                configFile.close()                                           

            elif jobChoice == "8":
                currentjob = jobList[7]
                print(f"You have succesfully got a job as a {currentjob.jobName}")

                config["hasJob"] = True
                config["currentJob"] = currentjob.jobName
                config["jobIndex"] = 7
                configFile =  open("config.json", "w")

                json.dump(config, configFile)

                configFile.close()

            elif jobChoice == "9":
                currentjob = jobList[8]
                print(f"You have succesfully got a job as a {currentjob.jobName}")

                config["hasJob"] = True
                config["currentJob"] = currentjob.jobName
                config["jobIndex"] = 8
                configFile =  open("config.json", "w")

                json.dump(config, configFile)

                configFile.close()
            else:
                print("The selected choice is wrong!")
        elif hasJob:
            def work(job, hoursToWork):

                if hoursToWork < 8 and hoursToWork > 0:

                    job = Job(currentConfigJob, job.jobSalary)
                    print(f"You are employed as a {job.jobName}")

                    input("If you want to work, then press any key: ")

                    print("You work...")
                    time.sleep(hoursToWork)

                    print(f"You have worked for {hoursToWork} hours")
                    print(f"You have earned {job.jobSalary * hoursToWork}$")

                    config["money"] += job.jobSalary * hoursToWork
                    configFile =  open("config.json", "w")
                    json.dump(config, configFile)

                    configFile.close()      

                else:
                    print("The number of hours has to be less than 8 and more than 0 hours you slaver")

            workChoice = "yes"
            while workChoice == "yes" or workChoice == "yes".capitalize:
                hoursToWork = int(input("How many hours do you want to work: "))

                work(currentjob, hoursToWork)

                workChoice = input("Do you want to work more?: ")
    mainChoice = input("Do you want to return to main menu?: ")

 