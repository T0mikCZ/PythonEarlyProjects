s = 0
while True:
    x = int(input("Napis cislo: "))

    if x == 0:
        print("Promenna s = " + str(s))
        break
    else:
        if x % 2 == 1:
            s += x
            print("Promenna x je liche cislo. Promenna \"s\" se zmenila a pokracuje se od zacatku")
        else:
            print("Promenna x je sude cislo. Promenna \"s\" se nezmeni a pokracuje se od zacatku cyklu")
            continue



#REFACTOR 20.01.2021

def algorithm(num):
    s = 0
    if num == 0:
        print(f"Promenna s = {s}")
        return num
    elif x % 2 == 1:
        s += num
    else:
        algorithm(num)