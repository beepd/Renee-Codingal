def process_range(a, b):
    squares = [i**2 for i in range(a, b + 1)]
    evens = [n for n in squares if n % 2 == 0]
    odds = [n for n in squares if n % 2 != 0]
    print(f"Even squares: {evens}")
    print(f"Odd squares: {odds}")
process_range(1, 10)
