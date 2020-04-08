"""

пример программы с ООП

данные класса
- имя
- фамилия
- возраст

"""
class PersonClass:
    first_name: str
    second_name: str
    age: int

user = PersonClass()
user.first_name = "Andy"
user.second_name = "APG"
user.age = 38

print(user.first_name, user.second_name, user.age)