def find_largest(num1, num2, num3):
    return max(num1, num2, num3)

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))
print("The largest number is:", find_largest(num1, num2, num3))
