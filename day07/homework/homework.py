
# Bank credit sistem(საბანკო სისტემა/მანქანის კრედიტი)
#fasi
car_price = 1000000     

print(car_price, 'you need for new car')


#რამდენი ფული არის საჭირო, და რამდენი გვაქვს
money_user = int(input('how much money you have now? '))
# სხვაობა
money_need = car_price - money_user    


if money_user < car_price:
    print('you need-',money_need)
    credit = input('if you wanna take credit with 12%? decide yes or no?')
    if credit == 'yes':
        credit_money = int(input('how much dollars you need?'))
        credit_time = int(input('how much years? '))

        overdraft = credit_money + credit_money * 12 / 100
        overdraft_years = overdraft * credit_time
        

        print('we need your pastort data')
        name = input('enter name:  ')
        surname = input('surname:  ')
        age = int(input('how old are you:  '))



        print(name, surname, age, '\n', 'your bill: ', "how much credit you taked", credit_money, "\n",'after ', credit_time, 'yesrs you need pay', overdraft_years )
    
    
    else:
        print('okay no problem')



else:
    print('you have enought money, congretulations')



    
