i = True

while i == True:
    num = int(input('enter your data: '))
    if num < 0:
        print('your number is negative')
    elif num == 0:
        print('your number is 0')
    else:
        print('your number is positive')
    
    stopword = input('do you wanna continue? yes or no? ')
    if stopword == "no":
        break

