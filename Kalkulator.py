import Math

print("Hlavni Menu")
print("1. Vypocita 2 cisla jakoukoliv operaci")
print("2. Vypocita list cisel")
print("3. Mocniny")
print("4. Tabulka nasobilky")


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

    for i in range(0,numberOfNumbers):

        numlist.append(int(input(f"Zadejte {i + 1}. cislo: ")))

    result = Math.CalculateList(numlist,operator)

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

    exit()