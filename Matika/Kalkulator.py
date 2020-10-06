import Math

#Functions
def fillListWithInput(numberOfNumbers):
    
    numlist = []

    for i in range(0,numberOfNumbers):

        numlist.append(int(input(f"Zadejte {i + 1}. cislo: ")))

    return numlist

#Main
print("Hlavni Menu")
print("1. Vypocita 2 cisla jakoukoliv operaci")
print("2. Vypocita list cisel")
print("3. Mocniny")
print("4. Tabulka nasobilky")
print("5. Prumer z listu cisel")
print("6. Najde Min a Max cislo v listu")


choice = input("Vyber cislo moznosti: ")

if choice == "1":
    num1 = int(input("Zadejte prvni cislo: "))
    num2 = int(input("Zadejte druhe cislo: "))
    operator = input("Zadejte operator: ")

    result = Math.calculate2Numbers(num1,num2,operator)

    print(f"{num1} {operator} {num2} = {result}")

elif choice == "2":
    numlist = []

    numberOfNumbers = int(input("Zadejte pocet cisel: "))
    operator = input("Zadejte operator: ")

    numlist = fillListWithInput(numberOfNumbers)

    result = Math.CalculateList(numlist, operator)

    print(f"Zadali jste tyto cislo: {numlist}")

    print(f"Vysledek = {result}")

elif choice == "3":
    num1 = int(input("Zadejte cislo: "))
    powNum = int(input("Zadejte mocninove cislo: "))

    result = Math.pow(num1, powNum)

    print(f"Mocnina {num1} na {powNum} = {result}")

elif choice == "4":

    size = int(input("Zadejte velikost: "))

    Math.mathTable(size)

elif choice == "5":

    numlist = []

    numberOfNumbers = int(input("Zadejte pocet cisel: "))

    numlist = fillListWithInput(numberOfNumbers)

    average = Math.average(numlist)

    print(f"Zadali jste tyto cislo: {numlist}")

    print(f"Prumer = {average}")

elif choice == "6":

    numlist = []

    numberOfNumbers = int(input("Zadejte pocet cisel: "))

    numlist = fillListWithInput(numberOfNumbers)

    min = Math.min(numlist)
    max = Math.max(numlist)

    print(f"Zadali jste tyto cislo: {numlist}")

    print(f"Nejmensi cislo = {min}")
    print(f"Nejvetsi cislo = {max}")


input()
exit()