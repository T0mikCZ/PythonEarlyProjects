def narcissistic(value):
    value = str(value)
    sum = 0
    for i in range(len(value)):
        sum += int(value[i])**len(value)
    value = int(value)
    if sum == value:
        return True
    else:
        return False
print(narcissistic(7))