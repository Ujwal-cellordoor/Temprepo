
user_input = int(input("Enter first number: "))
user_input1 = input("Enter operator: ")
user_input2 = int(input("Enter second number: "))


def addition(a, b):
    return a + b


def substraction(a, b):
    return a - b


def multiplication(a, b):
    return a * b


def calc():
    if user_input1 == "+":
        print("The ans is: " + addition(user_input, user_input2))
    elif user_input1 == "-":
        print("The ans is: " + str(user_input - user_input2))
    elif user_input1 == "/":
        print("The ans is: " + str(user_input / user_input2))
    elif user_input1 == "*":
        print("The ans is: " + str(user_input * user_input2))
    elif user_input1 == "%":
        print("The ans is: " + str(user_input % user_input2))


calc()
