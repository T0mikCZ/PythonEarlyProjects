class Student:
    def __init__(self, name, major, gpa, isOnProbation):
        self.name = name
        self.major = major
        self.gpa = gpa
        self.isOnProbation = isOnProbation
        
    def onHonorRoll(self):
        if self.gpa >= 3.5:
            return True
        else:
            return False


class Mobile:
    def __init__(self, name, OS, weight, version, colour):
        self.name = name
        self.OS = OS
        self.weight = weight
        self.version = version
        self.colour = colour