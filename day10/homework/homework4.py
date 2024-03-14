number1 = int(input('enter number 1: '))
number2 = int(input('enter number 2: '))


if number1 < number2:
    print('number1 < number2')
    bigger = number2
    smaller = number1
else:
    print('number1 > number2')
    bigger = number1
    smaller = number2

for i in range(smaller, bigger + 1, 2):
    print(i)