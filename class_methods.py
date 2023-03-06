print()

class User:

    activeUsers = 0

    @classmethod
    def from_string(cls,dataStr):
        username,name,surname,age=dataStr.split(",")
        return cls(username,name,surname,age)

    @classmethod
    def getActiveUsersCount(cls):
        return f"active user count : {cls.activeUsers}"
    
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

print(User.getActiveUsersCount())
# user1 = User("oguzhandr", "oguzhan", "durmaz", 23)
# user2 = User("burcukrk", "burcu", "kurak", 22)
# user3 = User("gkn0", "gokhan", "durmaz", 12)
# print(User.getActiveUsersCount())
# user3.logout()


user5=User.from_string("cozgr,ozgur,coskun,24")
print(User.getActiveUsersCount())
print(user5.username,user5.age)


print()