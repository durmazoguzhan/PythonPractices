class Car:
    def __init__(self, brand, model, year, price):
        self.brand=brand
        self.model=model
        self.year=year
        self.price=price
        print("car object created.")
        
car1=Car("Honda","Civic","2022",700000)
car2=Car("Audi","RS7","2020",1500000)

print(car1.brand,car1.price)
print(car2.brand,car2.price)