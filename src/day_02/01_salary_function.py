
def salary(hour: int, days: int):
    total = hour * days * 8
    final = total * .87

    return(total, " ", final)

print(salary(100, 1))
print(salary(100, 2))