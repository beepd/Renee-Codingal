def shutdown(user_choice):
    choice = user_choice.lower()
    if choice == "yes":
        print("shutting down")
    elif choice == "no":
        print("abort shut down")
    else:
        print("sorry")
user_input = input("Do you want to switch off the system? (Yes/No): ")
shutdown(user_input)