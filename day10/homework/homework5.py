jami = 0

num1 = int(input('enter number 1: '))
num2 = int(input('enter number 2: '))

if num1 < num2:
    big = num2
    small = num1
else:
    big = num1
    small = num2

for i in range(small, big + 1):
    jami = jami + i
    print(jami)


