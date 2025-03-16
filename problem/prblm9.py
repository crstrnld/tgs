def login_system(username, password):
    if username == "admin" and password == "admin123":
        return "Admin access granted"
    elif username == "user" and password == "user123":
        return "Limited access granted"
    elif username == "guest" and password == "":
        return "Minimal access granted"
    else:
        return "Access denied"

username = input("Enter username: ")
password = input("Enter password (leave blank for guest): ")
print(login_system(username, password))
