def digital_root(n):
    n = str(n)
    sum = 0
    for i in range(len(n)):
        sum += int(n[i])

    if len(str(sum)) == 1:
        return sum
    else:
        digital_root(sum)

print(digital_root(325))