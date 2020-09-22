def pyramida(velikost):
    j = 1

    for i in range(velikost,0,-1):
        print(" "*i, end = " ")
        print("* "*j)
        j+=1


def lidlPyramida(velikost):
    for i in range(0,velikost):
        for j in range(1,i):
            print("*")
        print()
print(pyramida(5))

def letterLoop(word):
    word = str(word)

    for letter in word:
        print(letter + " ", end = " ")

def raiseToPower(num, powNum):
    result = 1
    result2 = num**powNum
    
    for i in range(powNum):
        result *= num
    
    #return result
    return result2

print(raiseToPower(2,4))

letterLoop("abcdefghijklmnopqrsteuvwxyz")

input()