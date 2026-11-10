email = input("Enter email:")
if " " not in email and "@" in email and email.endswith(".com") and email[0] != "@":
    print("Valid Email")
else:
    print("Invalid Email")