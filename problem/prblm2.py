def is_even_or_odd(number):
    return "Even" if number % 2 == 0 else "Odd"

number = int(input("Enter a number: "))
print(is_even_or_odd(number))
