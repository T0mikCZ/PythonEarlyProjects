rebirth = int(input("Enter the number of rebirths: "))

multiplier = int(input("Enter a exp event multiplier you can leave it to 0 if there is no xp event: "))

print("Requierments for the next rebirth: " +  str(3000000 * rebirth - 1000000))

if multiplier == 0:
    print("Exp multiplier: " + str(0.2 * rebirth + 1.0))
else:
    print("Exp multiplier: " + str((0.2 * rebirth + 1.0) * multiplier))

input()