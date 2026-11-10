price = int(input("Enter price:"))
if price > 1000000:
   final_price = price - (price * 0.2)
elif price >= 500000:
   final_price =  price - (price * 0.1)
else:
    final_price = price
print("original price:", price )
print("Final price:", final_price)