numbers = [1, -3, 5, -7, 9, -12]
str_numbers = ["1", "3", "5", "7", "9", "12"]
names=["oguzhan","durmaz","hello","world","python","mechsoft"]

sqs = []

for number in numbers:
    sqs.append(number**2)

print(sqs)


def calcSqs(num):
    return num**2


result = list(map(calcSqs, numbers))
result = list(map(lambda num:num**2,numbers))
result=list(map(int,str_numbers))
result=list(map(abs,numbers))
result=list(map(float,numbers))
result=list(map(str.capitalize,names))
result=list(map(len,names))
print(result)

users=[
    {"name":"oguzhan","surname":"durmaz"},
    {"name":"ozgur","surname":"coskun"}
]

result=list(map(lambda x:x["name"],users))
print(result)