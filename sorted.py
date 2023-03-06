
numbers=[2,5,8,9,5,6,3]
print(numbers)

print(sorted(numbers))
print(sorted(numbers,reverse=True))
print(sorted((2,5,8,9,5,6,3)))

numbers.sort()
print(numbers)

#---------------------------------------#

users=[
    {"username":"oguzhandurmaz","posts":["post1","post2","post3"]},
    {"username":"burcukurak","posts":["post1","post2","post3","post4","post5"],"email":"burcukurak@gmail.com"},
    {"username":"atakanozden","posts":["post1","post2","post3","post4","post5","post6"]}
]
print(sorted(users,key=len))
print()
print(sorted(users,key=len,reverse=True))
print()
print(sorted(users,key=lambda user:user["username"]))
print()
print(sorted(users,key=lambda user:len(user["posts"]),reverse=True))