username = input("Enter username: ")
if len(username) >= 5 and " " not in username and username.isalpha() and username.islower():
    print("valid username")
else:
    print("invalid username")

