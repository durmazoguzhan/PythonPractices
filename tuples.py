#tuples=const lists

list1=[1,5,2,9]

myTuple=(1,4,"text",False)

print(type(list1))
print(type(myTuple))

print(list1[1])
print(myTuple[1])

print(list1)
print(myTuple)

print(len(list1))
print(len(myTuple))

list1[0]=3
print(list1)
# myTuple[0]=3 we can't do this because tuple is const.
# print(myTuple)

list1.append(60)
print(list1)
# myTuple.append(60) we can't do this because tuple is const.
# print(myTuple)

print(myTuple.count(5))
print(myTuple.index(4))

myTuple2=(1,3,"text2",True)
print(myTuple+myTuple2)

newList=tuple(list1)
print(newList)
print(type(newList))