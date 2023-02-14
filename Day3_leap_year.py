year = int(input("Which year do you want to check? "))
#logic here is leap year if its evenly divisible by 4 except #its evenly divisiable by 100 unless its divisible by 400.
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year.")
        else:
            print("Not leap year.")
    else:
        print("Leap year.")
else:
    print("Not leap year.")