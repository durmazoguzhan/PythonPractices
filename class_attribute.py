print()

class User:

    activeUsers = 0

    def __init__(self, username, name, surname, age):
        self.username = username
        self.name = name
        self.surname = surname
        self.age = age
        User.activeUsers += 1

    def getUserName(self):
        return self.username

    def logout(self):
        User.activeUsers-=1
        return f"{self.username} logged out."

print(f"Active Users Count: {User.activeUsers}")
user1 = User("oguzhandr", "oguzhan", "durmaz", 23)
user2 = User("burcukrk", "burcu", "kurak", 22)
user3 = User("gkn0", "gokhan", "durmaz", 12)
print(f"Active Users Count: {User.activeUsers}")
user3.logout()
print(f"Active Users Count: {User.activeUsers}")




print()