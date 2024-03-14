temp = int(input('enter your temperature in celius: '))
if temp > 30:
    print(temp, "your temp is hot")
elif temp < 30 and temp > 20:
    print(temp," your temp is normal")
elif temp < 20:
    print(temp, "your temp is cold")
else:
    print("EROR")
    