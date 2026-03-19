a = int(input("enter a value: "))
b = int(input("enter value 2 :"))
c = int(input("enter value 3: "))

a = a + b + c
b = a - b - c
c = a - b - c
a = a - b - c

print(a, b, c)