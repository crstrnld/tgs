def check_number_sign(number):
    if number > 0:
        return "Positive"
    elif number < 0:
        return "Negative"
    else:
        return "Zero"

number = float(input("Enter a number: "))
print(check_number_sign(number))
