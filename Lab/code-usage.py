Num = int(input('Enter your Loop'))
NumTotal = []
for i in range(Num):
    data = int(input('Enter your Data:'))
    NumTotal += [data]
print(NumTotal)
NumTotal.sort()
print(NumTotal)