def getRemainder(num, numDel):
    result = int(num / numDel)
    remainder = num - (result * numDel)
    return remainder

print(getRemainder(11, 6))