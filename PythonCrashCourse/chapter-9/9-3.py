class User():
    def __init__(self, first_name, last_name):
        self.first_name = first_name.title()
        self.last_name = last_name.title()

    def decribe_user(self):
        print(f"Your name is {self.first_name} {self.last_name}")

    def greet_user(self):
        print(f"Hello, {self.first_name} {self.last_name}")

user = User('lan','chunyuan')
user.greet_user()

user = User('leo','nado')
user.greet_user()