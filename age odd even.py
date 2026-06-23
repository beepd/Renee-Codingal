def check_age():
    user_input = input("Please enter your age: ")
    try:
        age = int(user_input)
        if age % 2 == 0:
            print(f"Your age ({age}) is an EVEN number.")
        else:
            print(f"Your age ({age}) is an ODD number.")
    except ValueError:
        # Catch the exception if the input wasn't a valid whole number
        print("Value Error: Invalid input! Please enter a valid integer (no decimals, letters, or special characters).")
if __name__ == "__main__":
    check_age()