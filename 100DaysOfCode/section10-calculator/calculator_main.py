#Calculator

#Add
def add(n1,n2):
    return n1 + n2

#Substract
def substract(n1,n2):
    return n1 - n2

#Multiply
def multiply(n1,n2):
    return n1 * n2

#Divide
def divide(n1,n2):
    return n1 / n2

operations = {
    "+": divide,
    "-": substract,
    "*": multiply,
    "/": divide
}


def calc(num1, num2, operator):
    operation = operations[operator]
    return operation(num1,num2)


def calculator():
    num1 = int(input("What's the first number?. "))
    next = True
    
    while next:
        print("Operations available to use:")
        for i in operations:
            print(i)
        operator = input(f"What's the operation you want use?")
        num2 = int(input("What's the second number?. "))
        print(f"{num1} {operator} {num2}")
        
        result = calc(num1, num2, operator)
        
        print(result)
        response = input("Do you want continue? y or n.").lower()
        
        if response == "y":
            num1 = result    
        else:
            print(f"Your calc finished: {result}")
            calculator()

calculator()
