# Calculating the bill amount between number of people to split the bill including the tip amount.

bill = float(input("Total Bill Amount?"))
tip_percent = float(input("% of tip you would like to give? 10%,15%,20% : "))
people_count = int(input("Number of people?"))
ind_bill = round((bill + (bill*(tip_percent/100)))/people_count,2)
print(f"Each person should pay {ind_bill} rupees")
