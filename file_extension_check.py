filename = input("Enter file name: ")
if filename.endswith(".pdf"):
    print("PDF")
elif filename.endswith(".jpg"):
    print("JPG")
else:
    print("Unknown file type")