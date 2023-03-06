carAudi = {
    "brand": "Audi",
    "model": "RS7",
    "year": 2019
}

print(carAudi)

# # accessing to values
# print(carAudi["brand"])
# print(carAudi.get("brand"))

# # if statements

# print("brand" in carAudi)
# print("engine" in carAudi)
# print(len(carAudi))

# # insert values
# carAudi["color"]="black"
# print(carAudi)

# # delete 

# carAudi.pop("year")
# print(carAudi)
# carAudi.popitem() #delete last item
# print(carAudi)
# del carAudi["brand"]
# print(carAudi)

# #del carAudi -> for delete the object

# #carAudi.clear()
# #print(carAudi)

# #object copying

# car=carAudi.copy()
# print(car)
# car["model"]="RS6"
# print(car)

# value updating
carAudi.update({
    "brand":"Volvo",
    "model":"S90"
})

print(carAudi)