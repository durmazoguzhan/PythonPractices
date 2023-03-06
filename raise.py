def users(username,city):
    cities=["istanbul","ankara","izmir","duzce","bolu","tokat"]
    if(type(username) is not str):
        raise TypeError("username have to be str type.")
    if(type(city) is not str):
        raise TypeError("city have to be str type.")
    if(city not in cities):
        raise ValueError("it's not true city.")
    
try:
    users("oguzhan","istanbul")
except Exception as e:
    print(e)
else:
    print("informations saved successfully.")