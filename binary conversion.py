# Get input from the user
decimal_num = int(input("Enter a decimal number: "))
temp_num = decimal_num
binary_str = ""
while temp_num > 0:
    remainder = temp_num % 2          
    binary_str = str(remainder) + binary_str  
    temp_num = temp_num // 2          
if decimal_num == 0:
    binary_str = "0"
print("The binary representation of",decimal_num,"is:",binary_str)