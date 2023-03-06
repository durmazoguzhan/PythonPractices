def userInfo(*args):
    print(type(args))

userInfo()

def userInfo(**kwargs):
    print(type(kwargs))
    print(kwargs)
    print("\n")
    for key,value in kwargs.items():
        print(f"{key} - {value}")

userInfo(username="oguzhand")
userInfo(username="oguzhand",password="123456",email="durmazoguzhan@yahoo.com")