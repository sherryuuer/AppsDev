# from art import logo
# print(logo)

#functions for calculations
def add(n1, n2):
    return n1 + n2

def subtract(n1,n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

# num1 = int(input("What's the first number?: "))
# def calculator(num1):
#     for key in operations:
#         print(key)
#     operation_symbol = input("Pick an operation from the line above: ")
#     num2 = int(input("What's the next number?: "))
#     function = operations[operation_symbol]
#     answer = function(num1, num2)
#     print(f"{num1} {operation_symbol} {num2} = {answer}")
#     return answer

# answer = calculator(num1)
# continue_cal = input(f"Type 'y' to continue calculating with {answer},or type 'n' to exit. ")
# while continue_cal == 'y':
#     answer = calculator(num1=answer)
#     continue_cal = input(f"Type 'y' to continue calculating with {answer},or type 'n' to exit. ")

new_cal = True
while new_cal:
    num1 = float(input("What's the first number?: "))
    continue_cal = True
    while continue_cal:
        for key in operations:
            print(key)
        operation_symbol = input("Pick an operation from the line above: ")
        num2 = float(input("What's the next number?: "))
        function = operations[operation_symbol]
        answer = function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        if input(f"Type 'y' to continue calculating with {answer},or type 'n' to start a new calculation. ") == "y":
            num1 = answer
        else:
            continue_cal = False



#use recurion to do this 
def calculator():
    num1 = float(input("What's the first number?: "))
    continue_cal = True
    while continue_cal:
        for key in operations:
            print(key)
        operation_symbol = input("Pick an operation from the line above: ")
        num2 = float(input("What's the next number?: "))
        function = operations[operation_symbol]
        answer = function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        if input(f"Type 'y' to continue calculating with {answer},or type 'n' to start a new calculation. ") == "y":
            num1 = answer
        else:
            continue_cal = False
            calculator() #you should be careful to do this
calculator()
