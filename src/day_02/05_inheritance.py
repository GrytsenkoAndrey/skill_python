'''

наследование
'''

class Person:
    first_name: str
    second_name: str
    age: int

    def __init__(self, first_name, second_name, age):
        self.first_name = first_name
        self.second_name = second_name
        self.age = age

    def info(self):
        print(f"{self.first_name} {self.second_name} {self.age}")

    def say(self, content):
        print(f"<{self.first_name}>: {content}")

class User(Person):
    password: str

    def check_pass(self, user_pass):
        return self.password == user_pass

user = User("John", "Doe", 38)
user.info()
user.say("Hello")

user.password = "123123"
print(user.check_pass("123123"))
