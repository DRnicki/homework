# დაწერეთ პროგრამა, რომელიც სთხოვს მომხმარებელს ორ რიცხვს და შეადარებს მათ.


while True:
    num1 = int(input('enter first data: '))
    num2 = int(input('enter second data: '))

    if num1 < num2:
        print(num1,'is lower then', num2)
    else:
        print(num2,'is lower then', num1)
        
        break
    

