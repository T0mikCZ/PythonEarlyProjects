def isPrime(num):
    if num == 2:
        return True
    elif num <= 1 :
        return False
    else:
        for i in range(2,num):
            if num % i == 0:
                return False
        return True

def getPrimes(num):
    for i in range(2,num+1):
        if isPrime(i):
            print(f"{i}")


getPrimes(10)