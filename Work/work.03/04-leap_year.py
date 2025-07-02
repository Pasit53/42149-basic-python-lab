years = int(input())
leap = str
if years % 4 == 0 :
    leap = "Leap Year"
elif years % 100 ==0 :
    if years % 400 == 0 :
        leap = "Leap Year"
else :
    leap = "Not a Leap year"
print(leap)