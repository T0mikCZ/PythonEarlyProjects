from Classes import Student, Mobile

student1 = Student("Tomas", "Programming", 3.2, False)
student2 = Student("Michal", "Art", 2.2, True)

redmi = Mobile("Redmi 7A", "MI11", 1.25, "11.0.4", "Blue" )

print(student1.major)
print(student2.major)
print(f"Mobile name: {redmi.name}, Version {redmi.OS} {redmi.version}, Colour: {redmi.colour}")