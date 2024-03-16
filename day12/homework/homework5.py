num = int(input('enter number from 1 until 9: '))

jamebi = 0

for i in range(1, 50 + 1):
    i *= num
    jamebi += num
    print(jamebi)

