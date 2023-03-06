list1=[1,2,3,4,5]
list2=["one","two","three","four","five"]
list3=['a','b','c','d','e']

# print(list(zip(list1,list3)))
# print(list(zip(list2,list3)))
# print(list(zip(list1,list2)))
# print(list(zip(list1,list2,list3)))

for item in zip(list1,list2,list3):
    print(item)
    
for x,y,z in zip(list1,list2,list3):
    print(x,y,z)