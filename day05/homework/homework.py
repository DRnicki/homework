# შექმენით ცვლადები 10 წიგნისთვის ( სახელი ცალკე, ფასი ცალკე, 
# 5 წიგნს გაუკეთეთ 10%იანი ფასდაკლება, 5 წიგნს გაუკეთეთ 20%იანი ფასდაკლება) 

books1 = "harry poter", "persi jackson", "shrek", "jumanji", "weathers child"
books2 = "money", "Ford", "Mcdonald", "vepxistyaosani", "remark"

price1 = 100
price2 = 200

discont1 = 10
discont2 = 20


print(books1, "have price:", price1)
print(books2, "have price", price2)

books_10_discount = price1 - price1 * discont1 / 100
books_20_discount = price2 - price2 * discont2 / 100

print(books1, ": price after discont will be: ", books_10_discount)
print(books2, ": price after discont will be: ", books_20_discount)
