text = input("Enter a text: ")
print("Characters:", len(text))
print("Number of a:", text.count("a"))
if text.startswith("A"):
    print("Yes")
else:
    print("No")