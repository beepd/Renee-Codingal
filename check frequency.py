test_dict = {'Codingal': 3, 'is': 2, 'best': 2, 'for': 2, 'Coding': 1}
print("Test Dictionary:", test_dict)
val = int(input("Enter the value to check for frequency: "))
frequency = list(test_dict.values()).count(val)
print(f"The frequency of value {val} is: {frequency}")