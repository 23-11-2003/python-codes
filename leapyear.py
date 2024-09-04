def is_leap(year):
    if year % 4 == 0:
        print("true")
    elif year % 100 == 0:
        print("false")
    elif year % 400 ==0:
        print("true")
    else:
        print("false")
year = int(input("enter"))
print(is_leap(year))