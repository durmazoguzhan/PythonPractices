ages=[7,15,18,23,27,35,45,60,65]

def isAdult(age):
    if(age<18):
        return False
    else:
        return True
    
result=list(filter(isAdult,ages))
result=list(filter(lambda x:x>=18,ages))

#----------------------------------------#

numbers=[10,30,25,50,80,72,36,90,33]
result=list(filter(lambda x:x%2==1,numbers)) ##odd numbers
result=list(filter(lambda x:x%2==0,numbers)) ##even numbers

#-----------------------------------------#

names=["oguzhan","ozgur","atakan","eren","burcu"]
result0=filter(lambda x:x[0]=='o',names)
result=list(map(lambda x:x.capitalize(),result0))

#------------------------------------------#

users=[
    {"username":"atakanozden","posts":[]},
    {"username":"oguzhandurmaz","posts":["post1","post2"]},
    {"username":"burcukurak","posts":["post1"]}
]

result=list(filter(lambda x:len(x["posts"])>0,users))

filteredResult=filter(lambda x:len(x["posts"])>0,users)
result=list(map(lambda x:x["username"],filteredResult))

result=[user["username"] for user in users if len(user["posts"])>0]

print(result)