while True:
    num = int(input("enter data (for stop enter 0): "))
    
    if num == 0:
        break
    
    divisible_by_2 = num % 2 == 0
    divisible_by_3 = num % 3 == 0
    
    if divisible_by_2 and divisible_by_3:
        print(num, "devisible on 2 and 3")
    elif divisible_by_2:
        print(num, "devisible on 2")
    elif divisible_by_3:
        print(num, "devisible on 3")
    else:
        print(num, "not devisible on 2 or 3")


# Reapeet this work___FORME