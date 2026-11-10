def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

import art

restart = True

while restart:
    print(art.logo)
    first_number = float(input("What's the first number?"))
    continue_calcuration = True
    while continue_calcuration:
        print("+\n-\n*\n/")
        picked_operation = input("Pick an operation: ")
        if picked_operation == "":
            pick_operation = "undefined"
        second_number = float(input("What's the next number?"))

        if picked_operation == "+":
            result = add(first_number, second_number)
        elif picked_operation == "-":
            result = subtract(first_number, second_number)
        elif picked_operation == "*":
            result = multiply(first_number, second_number)
        elif picked_operation == "/":
            result = divide(first_number, second_number)
        else:
            result = 0.0
        print(f"{first_number} {picked_operation} {second_number} = {result}")
        loop = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")
        if loop == "y":
            restart = False
            continue_calcuration = True
            first_number = result
        if loop == "n":
            restart = True
            continue_calcuration = False