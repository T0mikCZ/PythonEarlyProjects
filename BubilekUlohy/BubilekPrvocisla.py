def jePrvocislo(cislo):
    try:
        if(cislo == 2):
            print("Cislo {:,} je prvocislo".format(cislo).replace(",", " "))
        elif(cislo % 2 == 0):
            print("Cislo {:,} neni prvocislo".format(cislo).replace(",", " "))
        else:
            print("Cislo {:,} je prvocislo".format(cislo).replace(",", " "))
    except TypeError:
        print("Funkce muze prijimat jenom cisla")

try:
    cislo = int(input("Zadejte cislo: "))
except ValueError:
    print("Zadana moznost neni cislo!")
    input()
    exit()

jePrvocislo(cislo)

exit()
