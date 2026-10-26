import csv
a=("ich bin amir") #i am amir 
b=("ich bin 18 jahre alt") # i am 18 yers old
c= ("ich komme aus dem iran aus khozestan") #i am from iran originaly from khozesthan
with open("test.csv","w", newline="",
encoding="utf-8") as file:
 writer = csv.writer(file, delimiter="*")
 writer.writerow([a,b,c])

