
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

user = Person("John", "Doe", 38)
user.info()
user.say("Hello")