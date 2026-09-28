# Intentionally insecure code for security review
username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin" and password == "12345":
    print("Login successful")
else:
    print("Invalid username or password")
