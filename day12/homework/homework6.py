num1 = int(input('enter your number1: '))
num2 = int(input('enter your number2: '))

min = 0
max = 0

if num1 < num2:
   min = num1
   max = num2
else:
    min = num2 
    max = num1  
# max += num1  for another example

for i in range(min, max + 1, 1):
    print(i ** 3)