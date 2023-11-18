class Calculator:

    def __init__(self):
        pass
    def add(self, x, y):
        return x + y
    def subtract(self, x, y):
        return x - y
    def multiply(self, x, y):
        return x * y
    def divide(self, x, y):
        try:
            result = x / y
            if y == 0:
                raise ZeroDivisionError
            return result
        except ZeroDivisionError:
            return "Cannot divide by zero,plz change the value!"

# Calculator class instantiation
calculator = Calculator()

while True:
    try:
        num1 = float(input("first number: "))
        num2 = float(input("second number: "))
    except ValueError:
        print("invalid value plz check the value!")
        exit()

    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    try:
        choice = input("enter the opration( 1/ 2/ 3/ 4): ")
        if choice not in ['1', '2', '3', '4']:
            raise ValueError
    except ValueError:
        print("invalid option plz select the valid option!!")
        continue

    if choice == '1':
        result = calculator.add(num1, num2)
        print(f"The addition of the given numbers is: {result}")
    elif choice == '2':
        result = calculator.subtract(num1, num2)
        print(f"The subtraction of the given numbers is: {result}")
    elif choice == '3':
        result = calculator.multiply(num1, num2)
        print(f"The multiplication of the given numbers is: {result}")
    elif choice == '4':
        result = calculator.divide(num1, num2)
        print(f"The division of the given numbers is: {result}")

    try:
        user_choice = input("Do you want to continue? (yes/no): ").lower()
        if user_choice != 'yes' and user_choice != 'no':
            raise ValueError
    except ValueError:
        print("Invalid option. plz enter yes / no.")
        continue

    if user_choice == 'no':
        print("Exiting calculator. Thanks,Goodbye!")
        break

