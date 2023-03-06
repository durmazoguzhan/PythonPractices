print()

class User:
    
    # constructor method
    def __init__(self,username,name,surname,birthYear):
        # object attributes / instance attributes
        self.username=username
        self.name=name
        self.surname=surname
        self.birthYear=birthYear
    
    #instance methods
    def info(self):
        return f"{self.username} saved successfully."
    
    def calcAge(self):
        return f"{self.username} is {2023-self.birthYear} years old."
        
u1=User("oguzhandr","oguzhan","durmaz",1992)
u2=User("bkurak","burcu","kurak",2000)

print(u1.info())
print(u2.info())

print(u1.calcAge())
print(u2.calcAge())


print()