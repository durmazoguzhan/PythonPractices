# 34 -> istanbul
# 60 -> tokat

# cities=["istanbul","tokat"]
# plateCodes=[34,60]
# print(plateCodes[0],cities[0])
# print(plateCodes[1],cities[1])
# print(plateCodes[cities.index("tokat")])

# dictionaries -> key-value

# cities={"istanbul":34,"izmir":35,"tokat":60,"duzce":81}
# print(cities["duzce"])

# cities["eskisehir"]=26
# cities["ankara"]=6
# print(cities)

products = {
    100: {
        "productName": "Monitor",
        "productDescription": "16 inc",
        "warranty": 3,
        "price": [800, 944]
    },
    101: {
        "productName": "SSD",
        "productDescription": "256GB",
        "warranty": 2,
        "price": [1500, 1770]
    },
}

print(products)
print(type(products))
print(products[100])
print(products[100]["productName"])

totalPrice = products[100]["price"][1]+products[101]["price"][1]
print(totalPrice)
