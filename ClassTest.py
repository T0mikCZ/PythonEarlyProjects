from Classes import Student, Mobile

student1 = Student("Tomas", "Programming", 3.6, False)
student2 = Student("Michal", "Art", 2.2, True)

redmi = Mobile("Redmi 7A", "MI11", 1.25, "11.0.4", "Blue" )

print(student1.major)
print(student2.major)

print(f"{student1.name} has honor: {student1.onHonorRoll()}")
print(f"{student2.name} has honor: {student2.onHonorRoll()}")

print(f"Mobile name: {redmi.name}, Version: {redmi.OS} {redmi.version}, Colour: {redmi.colour}")

name = input("Zadejte jmeno mobilu: ")
OS = input("Zadejte operacni system: ")
weight = input("Zadejte vahu: ")
version = input("Zadejte verzi mobilu: ")
colour = input("Zadejte barvu mobilu: ")


newPhone = Mobile(name, OS, weight, version, colour)

print(f"Mobile name: {newPhone.name}, Version: {newPhone.OS} {newPhone.version}, Colour: {newPhone.colour}, Weight: {newPhone.weight}")