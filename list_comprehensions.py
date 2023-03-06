# numbers=[]
# for i in range(10):
#     numbers.append(i)
# print(numbers)

# expression for item in list

# numbers = [i for i in range(10)]
# print(numbers)

# numbers = [i*2 for i in range(10)]
# print(numbers)

# numbers = [i*i for i in range(10)]
# print(numbers)

# list1 = [3, 8, 5, 12, 40]
# # numbers = [i*2 for i in list1]
# # print(numbers)

# # result=[str(number) for number in list1]
# # print(result)

# name="MechSoft"
# print(name)
# result=[a.upper() for a in name]
# print(result)

# names=["Oguzhan","Durmaz","MechSoft"]
# result=[letter.lower() for letter in names]
# print(result)
# result=[letter.upper() for letter in names]
# print(result)

x = 1
y = 1
z = 1
n = 2
    
result=[[a,b,c] for a in range(x+1) for b in range(y+1) for c in range(z+1) if a+b+c!=n]
    
print(result)