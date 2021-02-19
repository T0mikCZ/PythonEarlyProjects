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


#REFACTOR 20.01.2021

def isPrime(num):
    if num <=1:
        return False
    elif num == 2:
        return True
    else:
        for i in range(2,num):
            if num % i == 0:
                return False
        return True
