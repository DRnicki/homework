password = "12345678"
truepass = True
while truepass:
    if input('enter your password: ') == password:
        truepass = False
        print('authorization was successful')
    else:
        print('authorization failed')
        
        