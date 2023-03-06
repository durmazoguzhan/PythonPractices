print()

# parent class / base class
class Person:
    counter1=0
    def __init__(self,name,surname,age):
        self.name=name
        self.surname=surname
        self.age=age
        print("person object created.")
        
    def info(self):
        print(self.name,self.surname,self.age)

# child class
class Student(Person):
    def __init__(self, name, surname, age, number):
        super().__init__(name, surname, age)
        self.number=number
        print("student object created.")

# child class
class Teacher(Person):
    def __init__(self, name, surname, age, branch):
        super().__init__(name, surname, age)
        self.branch=branch
        print("teacher object created.")

t1=Teacher("oguzhan","durmaz",35,"maths")
t1.info()
s1 = Student("ozgur","coskun",24,"182120005")
s1.info()


print()
