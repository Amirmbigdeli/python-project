a=12
b=float(a)
c=str(b)
print(c)
print(f"the value is {c}")
flower=("roz")
print(flower)
def sabzi():
    global flower
    flower = ("orkideh")
sabzi()
print(flower) 