def determine_grade(score):
    if 80 <= score <= 100:
        return "A"
    elif 70 <= score < 80:
        return "B"
    elif 60 <= score < 70:
        return "C"
    elif 50 <= score < 60:
        return "D"
    else:
        return "E"

score = int(input("Enter test score (0-100): "))
print("Grade:", determine_grade(score))
