#TODO Kupovani jidla a piti DONE
#TODO Doplnovani energie DONE

#Promenne Hrace
food = 100
drink = 100
hp = 100
money = 0
energy = 100
haveJob = False

#Job Promenne
jobList = ["Obsluha v McDonald", "Uklizecka", "Pracovnik v Prikopu"]
jobMoney = [10,15,25]
currentJob = ""
currentJobMoney = 0
currentJobEnergy = currentJobMoney

#Dalsi Promenne
mainLoopChoice = "ano"

#Hlavni Cykl
while mainLoopChoice == "ano" or mainLoopChoice.capitalize():

    #Dulezite Staty
    print("\nPocet Zivotu: " +  str(hp))
    print("Pocet Jidla: " + str(food))
    print("Pocet Piti " + str(drink))
    print("Pocet Energie " + str(energy))
    print("Pocet Penez " + str(money) + "\n")

    #Hlavni Menu
    print("Hlavni Menu")
    print("1. Jit do prace")
    print("2. Jit do obchodu")

    choice = input("\nZadejte moznost: ")

    #Moznosti

    #Moznost 1
    if choice == "1":
    
        #Pokud Nema Praci
        if not haveJob:
            print("\nNejdrive si musis najit praci")
            print("Vyber si Praci: ")

            print("1. Obsluha v McDonald (10 penez za den)")
            print("2. Uklizecka (15 penez za den)")
            print("3. Pracovnik v prikopu (25 penez za den)")

            jobChoice = input("\nZadej cislo prace pro vybrani prace: ")

            while not haveJob:
                
                if jobChoice == "1":
                    print("\nUspesne si se zamestnal jako obsluha v McDonald")
                    haveJob = True
                    currentJob = jobList[0]
                    currentJobMoney = jobMoney[0]
                    currentJobEnergy = currentJobMoney
                elif jobChoice == "2":
                    print("\nUspesne si se zamestnal jako uklizecka")
                    haveJob = True
                    currentJob = jobList[1]
                    currentJobMoney = jobMoney[1]
                    currentJobEnergy = currentJobMoney
                elif jobChoice == "3":
                    print("\nUspesne si se zamestnal jako pracovnik v prikopu")
                    haveJob = True
                    currentJob = jobList[2]
                    currentJobMoney = jobMoney[2]
                    currentJobEnergy = currentJobMoney
                else:
                    print("\nSpatne Zadana moznost!")
                    break
        #Pokud Ma Praci
        else:
            print("\nJsi zamestnan jako: " + currentJob)

            goWorkChoice = input("\nJit pracovat (ano/ne)?: ")

            if goWorkChoice == "ano" or mainLoopChoice.capitalize() and energy > 0:
                workMore = "ano"

                while workMore == "ano" or mainLoopChoice.capitalize() and energy > 0:
                    print("Pracujes")
                    input()
                    print("Vydelal jsi: " + str(currentJobMoney) + "KC")
                    money += currentJobMoney
                    energy -= currentJobEnergy

                    if energy > 0:

                        workMore = input("Pracovat dal (ano/ne)?: ")
                    else:
                        print("Nemas dost Energie!")
            else:
                print("Nemas dost energie!")

    #Moznost 2
    if choice == "2":
        print("Jsi v obchode\n")
        print("1.Koupit jidlo")
        print("2.Koupit piti")
        print("3.Koupit energy drink")

        storeChoice = input("Vyber co si chces koupit: ")

        if storeChoice == "1" and food < 100 and energy < 100:
            if money >= 15:
                money -= 15
                food += 15
                energy += 5
                print("Uspesne jsi koupil jidlo za 15 KC\n")
            else:
                print("Nemas dostatek penez")
        elif storeChoice == "2" and drink < 100 and energy < 100:
            if money >= 15:
                money -= 15
                drink += 15
                energy += 5
                print("Uspesne jsi koupil piti za 15 KC\n")
            else:
                print("Nemas dostatek penez")
        elif storeChoice == "3" and energy < 100:
            if money >= 25:
                money -= 15
                drink -= 15
                food -= 10
                energy += 20
                print("Uspesne jsi koupil energy drink za 15 KC\n")
            else:
                print("Nemas dostatek penez")
        else:
            print("Nektere staty mas na max nebo nemas penize")

    #Vraceni do hlavniho menu
    mainLoopChoice = input("\nChcete se vratit do menu (ano/ne)?: ")
