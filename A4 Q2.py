a = int(input("Enter the year to check "))
i = 0
if a%4==0:
    if a%100==0:
        b = a//100
        if b%4==0:
            print("Its a leap year")
        else:
            print("Its not a leap year")
