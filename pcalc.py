# deine the functions needed: add, sub, mult, divi
# print options to the user
# ask for values
# call the funcntions
# while loop to contine the program untoll the user wants to exit


import os


def add(value1, value2):
    return value1 + value2


def sub(value1, value2):
    return value1 - value2


def mul(value1, value2):
    return value1 * value2


def div(value1, value2):
    return value1 / value2


def renderOptions():
    print("1. Add")
    print("2. Sub")
    print("3. Mul")
    print("4. Div")
    print("5. Quit")


def getOperation():
    return input("Select operation: ")


def getValue():
    return input("Enter value: ")


def calculate(operation, value1, value2):
    match int(operation):
        case 1:
            return add(value1, value2)
        case 2:
            return sub(value1, value2)
        case 3:
            return mul(value1, value2)
        case 4:
            return div(value1, value2)


def clear_console():
    os.system("cls" if os.name == "nt" else "clear")


def main():
    run = True
    while run:
        print("\==== pCalc ====\n")
        renderOptions()
        operation = getOperation()
        run = int(operation) != 5
        if run:
            value1 = int(getValue())
            value2 = int(getValue())
            sum = calculate(operation, value1, value2)
            print(f"\nSum is: {sum}\n")


if __name__ == "__main__":
    main()
