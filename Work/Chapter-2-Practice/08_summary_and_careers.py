bill = float(input())
tip_percent = int(input())
people = int(input())

total = bill + (bill * tip_percent / 100)
per_person = total / people
output = round(per_person,2)
print("Each person pays:",output)