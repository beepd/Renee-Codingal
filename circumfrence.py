def calculate_circumference(radius):
    return 2 * 3.14159 * radius
radius = float(input("Enter the radius of the circle: "))
result = calculate_circumference(radius)
print(f"The circumference of a circle with radius {radius} is: {result}")