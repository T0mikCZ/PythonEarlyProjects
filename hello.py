num1 = int(input("Type your first number: "))

num2 = int(input("Type your second number: "))

mathOperator = input("Type a math operator (+-*/): ")

if mathOperator == "+":
    print(str(num1) + "+" + str(num2) + "=" + str(num1 + num2))

elif mathOperator == "-":
    print(str(num1) + "-" + str(num2) + "=" + str(num1 - num2))

elif mathOperator == "*":
    print(str(num1) + "*" + str(num2) + "=" + str(num1 * num2))

elif mathOperator == "/":
    if num2 == 0:
        print("Error you can't divide by zero")
    else:
        print(str(num1) + "/" + str(num2) + "=" + str(num1 / num2))
else:
    print("Error!")

input()