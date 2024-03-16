print('1. km - miles')
print('2. miles - km')

choise = int(input('enter 1 or 2: '))
distance = float(input('enter distance: '))

if choise == 1:
    print(distance / 1.6)
elif choise == 2:
    print(distance * 1.6)
else:
    print('wrong choise')
    

