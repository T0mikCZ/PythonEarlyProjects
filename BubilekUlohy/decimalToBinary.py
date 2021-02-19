def toBinary(num):
    if num < 1:
        return 1
    print(num%2)
    num = int(num / 2)
    toBinary(num)

print(toBinary(2))