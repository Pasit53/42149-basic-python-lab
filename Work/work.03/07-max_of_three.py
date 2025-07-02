numbera = int(input())
numberb = int(input())
numberc = int(input())
max = numbera
if numberb > numbera :
    max = numberb
    if numberc > numberb :
        max = numberc
print(max)