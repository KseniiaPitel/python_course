import sys
a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])
#a = input("Enter a ")
#b = input("Enter b ")
#c = input("Enter c ")

a = float(a)
b = float(b)
c = float(c)

D: float = b ** 2 - (4 * a * c)

#print(D)
if D > 0:
    x1 = (-b + (D) ** 0.5) / (2 * a)
    x2 = (-b - (D) ** 0.5) / (2 * a)
    print(int(x1))
    print(int(x2))
elif D == 0:
    x1 = x2 = (-b) / (2 * a)
    print(int(x1))
    print(int(x2))
else:
    print("D<0")
