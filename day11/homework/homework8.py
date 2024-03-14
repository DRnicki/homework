result = int(input('enter your ressults value: '))

if result > 90:
    print('your mark is A')
elif result < 89 and result > 80:
    print('your mark is B')
elif result < 79 and result > 70:
    print('your mark is C')
elif result < 69 and result > 60:
    print('your mark is D')
elif result < 60:
    print('your mark is F')