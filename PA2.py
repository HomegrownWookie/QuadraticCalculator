import math

a = int(input("Enter A: "))
b = int(input("Enter B: "))
c = int(input("Enter C: "))

disc = (b * b) - 4 * a * c

if disc < 0:
    print("Complex Number!")
    exit()

if a == 0:
    print("Not a quadratic function.")
    exit()

x1 = (-b + int(math.sqrt(disc))) / (2 * a)
x2 = (-b - int(math.sqrt(disc))) / (2 * a)

print("Roots: ", x1, x2)

'''
A   B   C   Roots
2   -1  -1  (1, -0.5)
1   4   4   (-2, -2)
3   11  0   (0, -3.665)
4   0   8   Complex Number!
0   4   4   Not a quadratic function.
'''