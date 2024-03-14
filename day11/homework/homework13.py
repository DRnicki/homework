number = 0
num_bigger_75 = 0
while number < 100:
    number += 1
    if number > 50 and number % 2 != 0:
        print("რიცხვები რომელიც მეტია 50ზე და არიან კენტები: ",number)
    if number > 75 and number % 2 != 0:
        num_bigger_75 += number
print("jami",num_bigger_75)

        
 
            