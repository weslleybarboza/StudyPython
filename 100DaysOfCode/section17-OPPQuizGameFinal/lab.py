class User:

    def __init__(self, id, username):
        self.id = id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = User("001", "weslley")
user_2 = User("002", "thaisa")

user_1.follow(user_2)

print(user_1)
print(user_1.username)
print(user_1.following)
print(user_1.followers)

print(user_2)
print(user_2.username)
print(user_2.following)
print(user_2.followers)
