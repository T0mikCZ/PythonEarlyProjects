velikost = int(input("Zadejte velikost: "))

velikost += 1

for i in range(1,velikost,1):
    for j in range(1,velikost,1):
        print(i * j, end = " ")

    print("X" + str(i))

input()