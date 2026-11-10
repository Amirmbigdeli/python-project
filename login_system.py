username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin" and password == "123456":
    print("Login successful")

elif username != "admin" and password != "123456":
    print("Invalid username and password")

elif username != "admin":
    print("Invalid username")

else:
    print("Invalid password")