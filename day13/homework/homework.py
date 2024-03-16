user_age = int(input('enter your age: '))

if user_age < 18:
    print("You are a minor")
elif user_age > 18 and user_age < 65:
    print('you are adult')
else:
    user_age > 65
    print('you are senior sitizen')
