
hour_price = int(input("введите стоимость часа >>>"))
days = int(input("введите количество дней (рабочих) >>>"))

total = hour_price * days * 8
final = total * .87

print(total, " ", final)