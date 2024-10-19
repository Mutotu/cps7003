# Example of 1-tier architecture
# user interface => command-line interaction where the user selects an operation and inputs numbers
# Business logic => in the functions of add, subtract, multiply, divide

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0: return "Error! Division by zero"
    x / y

def main():
    print("Simple Calculator")
    print("Select operation")
    print("1: Add, 2: Subtract, 3: Multiply, 4: Divide")

    choice = input("Enter choice(1/2/3/4)")

    if choice in ["1", "2", "3", "4"]:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == "1"  : print(f"{num1} + {num2} = {add(num1, num2)}")
        elif choice == "2": print(f"{num1} - {num2} = {subtract(num1, num2)}")
        elif choice == "3": print(f"{num1} * {num2} = {multiply(num1, num2)}")
        elif choice == "4": print(f"{num1} / {num2} = {divide(num1, num2)}")
        else: print("Invalid Input")

if __name__ == "__main__":
    main()

