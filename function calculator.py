def calculator():
    while True:
        try:
            num1 = float(input("Enter the first number: "))
            operator = input("Enter an operator (+, -, *, /): ")
            if operator not in ['+', '-', '*', '/']:
                print("Error: Invalid operator. Please use +, -, *, or /.\n")
                continue
            num2 = float(input("Enter the second number: "))
            if operator == '+':
                result = num1 + num2
            elif operator == '-':
                result = num1 - num2
            elif operator == '*':
                result = num1 * num2
            elif operator == '/':
                if num2 == 0:
                    raise ZeroDivisionError
                result = num1 / num2
            print(f"Result: {num1} {operator} {num2} = {result}\n")
        except ValueError:
            print(" Error: Invalid input. Please enter valid numbers or exact operators.\n")
        except ZeroDivisionError:
            print("Error: Division by zero is not allowed.\n")
        except Exception as e:
            print(f"An unexpected error occurred: {e}\n")
if __name__ == "__main__":
    calculator()