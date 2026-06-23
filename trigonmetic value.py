import math

def calculate_trig_values():
    print("--- Trigonometric Calculator ---")
    try:
        degrees = float(input("Enter the angle in degrees: "))
        radians = math.radians(degrees)
        sin_value = math.sin(radians)
        cos_value = math.cos(radians)
        tan_value = math.tan(radians)
        print(f"\nResults for {degrees}°:")
        print(f"  * Sine (sin):    {round(sin_value, 4)}")
        print(f"  * Cosine (cos):  {round(cos_value, 4)}")
        print(f"  * Tangent (tan): {round(tan_value, 4)}")
    except ValueError:
        print("Error: Please enter a valid numerical value for the angle.")
if __name__ == "__main__":
    calculate_trig_values()