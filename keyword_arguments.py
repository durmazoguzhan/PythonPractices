def fullName(firstName,lastName):
    return f"Welcome to system, {firstName} {lastName}"

result=fullName("Oguzhan","Durmaz")
result=fullName("Durmaz","Oguzhan")
result=fullName(lastName="Durmaz",firstName="Oguzhan")

print(result)