class User:

    def __init__(self, user_id: int, name: str):
        self.id = user_id
        self.name = name
        self.followers = 0
        self.following = 0

    def greet(self):
        print(f"Hello! my name is {self.name}!")

    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = User(1, 'Leo')
user_2 = User(2, 'Sunny')

user_1.greet()
user_2.greet()

user_1.follow(user_2)
user_2.follow(user_1)
