cislo1 = int(input("Zadejte cislo: "))

cislo2 = int(input("Zadejte dalsi cislo: "))

operator = input("Zadejte operator (+-*/)")

if operator == "+":
    print(f"{cislo1} {operator} {cislo2} = {cislo1 + cislo2}")    
elif operator == "-":
    print(f"{cislo1} {operator} {cislo2} = {cislo1 - cislo2}")
elif operator == "*":
    print(f"{cislo1} {operator} {cislo2} = {cislo1 * cislo2}")
elif operator == "/":
    if cislo2 == 0:
        print("Nemuzes delit nulou")
    else:
        print(f"{cislo1} {operator} {cislo2} = {cislo1 * cislo2}")
else:
    print("Spatny operator!")