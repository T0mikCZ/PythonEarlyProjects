limit = 30
haler = 1
formatHaler = "{:,}".format(haler) #Formatuje cislo, aby melo carky

print(f"1.den: {haler} halir")

#Main For Loop
for i in range(2,limit + 1):
    haler *= 2
    formatHaler = "{:,}".format(haler)

    print(f"{i}.den: {formatHaler} haliru")
#For loop End
koruna = int(haler / 100)
formatKoruna = "{:,}".format(koruna) #Formatuje cislo, aby melo carky

print(f"Finalni penize v halirech: {formatHaler} haleru")
print(f"Finalni penize v korunach: {formatKoruna} korun")