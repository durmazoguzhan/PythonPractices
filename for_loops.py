# numbers=[10,20,30,50,70,100]

# # like for-each in java,c#
# for number in numbers:
#     print(number)

# name="Oguzhan"

# for letter in name:
#     print(letter)

# myTuple=[(1,2),(3,4),(5,6)]

# for a,b in myTuple:
#     print(a,b)

# for a in myTuple:
#     print(a)

cities = {"06": "ankara", "34": "istanbul", "35": "izmir", "60": "tokat"}

# for city in cities:
#     print(cities[city])

# for city in cities.values():
#     print(city)

for code, cityName in cities.items():
    print(code+" - "+cityName)
