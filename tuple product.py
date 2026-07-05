def calculate_product(numbers):
    result = 1
    for x in numbers:
        result *= x
    return result

# Data from the image
numbers_1 = (4, 3, 2, 2, -1, 18)
numbers_2 = (2, 4, 8, 8, 3, 2, 9)

# Calculating and printing results
print("Product of first set:", calculate_product(numbers_1))
print("Product of second set:", calculate_product(numbers_2))
