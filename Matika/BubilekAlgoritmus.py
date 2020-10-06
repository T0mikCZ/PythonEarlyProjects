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