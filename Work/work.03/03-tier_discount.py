price = float(input())
sum = 0
if price >= 2000 :
    sum = price*(85/100)
elif price >= 1000 :
    sum = price*(90/100)
elif price >= 500 :
    sum = price*(95/100)
else :
    sum = price
print (sum)