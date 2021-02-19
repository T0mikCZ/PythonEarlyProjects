import random as rn

randomList = []

def generateList(emptyList):

    for _ in range(10):
        randomNum = rn.randint(0,1000)
        emptyList.append(randomNum)

def writeList(array):
    for i,element in enumerate(array):
        print(f"{i+1}. {element}")

def average(array):
    sum = 0
    for element in array:
        sum += element
    return sum / len(array)

generateList(randomList)
writeList(randomList)

print(f"Min = {min(randomList)}")
print(f"Max = {max(randomList)}")
print(f"Average = {average(randomList)}")
print(randomList)
randomList.sort()
print(randomList)


