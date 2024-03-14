# format 1 long version

positive = True

num = 0

# while positive = True:
while positive:
    nums = int(input('enter your data'))
    num += nums
    if nums < 0:
        positive = False
print(num)

# format 2

sum = 0

while True:
    num = input('enter your data')
    if num < 0:
        break
    # აქ უფრო მოკლედ შეიძლებბა ჩაწერა break ოპერატორის მეშვეობით
    sum += num

print('your data sum together is: ',sum)



    