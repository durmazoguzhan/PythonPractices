cities=["istanbul","ankara","duzce","izmir","bursa"]
print(cities)
print(cities[-1])
print(cities[0:2])
print(cities[2:])
print(cities[:3])
print(cities[-3:-1])

cities[0]="tokat"
print(cities)

print(len(cities))

del cities[0]
print(cities)