amount = int(input("Enter bill amount: "))
tipP = int(input("Enter tip percent: "))

def tip():
    tipA = (tipP/100)*amount
    total = tipA + amount
    return total

a = tip()
print("Total amount to pay: ", a)