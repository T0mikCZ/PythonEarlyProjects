def max(numberList):

    maximum = numberList[0]

    for i in range(len(numberList)):
        if maximum > numberList[i]:
            maximum = numberList[i]

    return maximum

def min(numberList):

    minimum = numberList[0]

    for i in range(len(numberList)):
        if minimum < numberList[i]:
            minimum = numberList[i]

    return minimum

def pow(number, powNumber):

    return number ** powNumber


def average(numberList):

    average = 0

    for i in range(len(numberList)):

        average += numberList[i]

    return average / len(numberList)

def CalculateList(numberList, operator):
    result = 0

    if operator == "+":
        for i in range(len(numberList)):
            result += numberList[i]
        return result
    elif operator == "-":
        for i in range(len(numberList)):
            result = numberList[0]
            result -= numberList[i]
        return result
    elif operator == "*" or operator == "x":
        for i in range(len(numberList)):
            result = numberList[0]
            result *= numberList[i]
        return result
    elif operator == "/":
        for i in range(len(numberList)):
            result = numberList[0]
            result /= numberList[i]
        return result
    elif operator == "%":
        for i in range(len(numberList)):
            result = numberList[0]
            result /= numberList[i]

            rest = numberList[0]
            rest %= numberList[i]
        return int(result), rest
    else:
        return "Error: Wrong Operator"

def floor(number):
    return int(number)


def calculate2Numbers(number1, number2, operator):

    if operator == "+":
        return number1 + number2
    elif operator == "-":
        return number1 - number2
    elif operator == "*" or operator == "x":
        return number1 * number2
    elif operator == "/":
        return number1 / number2
    elif operator == "%":
        return int(number1 / number2), number1 % number2
    else:
        return "Error: Wrong Operator"

def mathTable(size):

    size +=1
    for i in range(1,size):
        for j in range(1,size):
            print(i * j, end = " ")

        print(f"X {i}")