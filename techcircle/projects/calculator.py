def add(a, b):
    return a + b

def mutiply(a, b):
    return a * b

def subtract(a, b):
    return a - b

def divide(a, b):
    return a / b


while True:
    num1 = int(input("enter a number: "))
    num2 = int(input("enter a number: "))

    print("Which operation do u which to perform ")
    print("1: Add the two numbers")
    print("2: subtract the two numbers")
    print("3: Mutiply the two numbers")
    print("4: Divide the two numbers")
    print("5: exit")

    op = int(input("Enter a the number for the operation: "))

    if op == 1:
       print(add(num1, num2))
    elif op == 2:
        print(subtract(num1, num2))
    elif op == 3:
        print(mutiply(num1, num2))
    elif op == 4:
        print(divide(num1, num2))
    elif op == 5:
        print("Good bye")
        break
    else:
        print("invalid operation number")
