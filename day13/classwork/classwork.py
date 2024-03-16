user_age = int(input('enter your age: '))

if user_age >= 0 and user_age < 18:
    print('you are child')
elif user_age > 18 and user_age < 50:
    print("you are adult")
else:
    print('you are old')