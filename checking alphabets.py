x = input("Enter a character: ")
is_lower = x >= 'a' and x <= 'z'
is_upper = x >= 'A' and x <= 'Z'
if is_lower or is_upper:
    print("The input is an alphabet.")
else:
    if not (is_lower or is_upper):
        print("The input is NOT an alphabet.")