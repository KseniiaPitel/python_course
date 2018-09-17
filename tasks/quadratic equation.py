a = input("Enter a ")
a = float(a)
b = input("Enter b ")
b = float(b)
c = input("Enter c ")
c = float(c)

D: float = b ** 2 - (4 * a * c)

if D > 0:
    x1 = (-b + (b ** 2 + 4 * a * c) ** 0.5) / (2 * a)
    x2 = (-b - (b ** 2 + 4 * a * c) ** 0.5) / (2 * a)
    print(x1)
    print(x2)
elif D == 0:
    x1 = x2 = (-b)/(2*a)
    print(x1)
    print(x2)
else:
    print("D<0")
