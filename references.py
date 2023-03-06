# value types -> string, number
num1 = 10
num2 = 20
num1 = num2
num2 = 30
print(num1, num2)

# reference types -> lists
list1 = ["python", "java"]
list2 = ["python", "java"]
list1 = list2
list2[0] = "kotlin"
print(list1, list2)
