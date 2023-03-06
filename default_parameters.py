
def sayWelcome(name="User",message="Welcome"):
    print(f"{message} {name}")
    
sayWelcome("Oguzhan","Good morning")
sayWelcome("Oguzhan")
sayWelcome()

def sumNumbers(num1,num2):
    return num1+num2

def multiplyNumbers(num1,num2):
    return num1*num2

def operation(num1,num2,function):
    return function(num1,num2)

def numMultiplyNum(num1):
    return num1*num1

print(numMultiplyNum(sumNumbers(1,2)))

print(operation(10,20,multiplyNumbers))