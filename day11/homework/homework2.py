i = True

nums = 0

while i:
    number = input('enter your data: ')
    if number == "0":
        i = False
    else:
        nums += int(number)
print(nums)

# ამ პროგრამამ მაგარი გამაწვალა მაგრამ მაინც შევძელი))) 
# მთავარი იყო რომ რიცხვები რომ შემოგქონა მიგვეღო str ში. იმიტომ რომ int ზე არ აჩერებდა while 
# და ინტეჯერად გადამეკეთებინა იკვე თვითომ number-ი შეკრების დროს.