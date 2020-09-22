numList = [5,2,3,1,0]

def sayHi(name):
    return "Hello " + name

def plus(num1, num2):
    return num1 + num2

def min(listCisel):
    min = listCisel[0]

    for i in range(0,len(listCisel)):
        if listCisel[i] < min:
            min = listCisel[i]
        else:
            min = min
    
    return min

def max(listCisel):
    max = listCisel[0]

    for i in range(0,len(listCisel)):
        if listCisel[i] > max:
            max = listCisel[i]
        else:
            max = max
    
    return max

print(min(numList))
print(max(numList))