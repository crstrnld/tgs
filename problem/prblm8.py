def check_triangle(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        if a == b == c:
            return "Equilateral Triangle"
        elif a == b or a == c or b == c:
            return "Isosceles Triangle"
        else:
            return "Scalene Triangle"
    else:
        return "Not a Triangle"

a = float(input("Enter first side length: "))
b = float(input("Enter second side length: "))
c = float(input("Enter third side length: "))
print(check_triangle(a, b, c))
