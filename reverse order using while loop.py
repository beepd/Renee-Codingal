number = int(input("Enter a number: "))
count = 0
if number < 0:
    number = number * -1

# Special case for zero
if number == 0:
    count = 1
else:
    while number > 0:
        number = number // 10  # Removes the last digit
        count += 1
print(f"The number of digits is: {count}")