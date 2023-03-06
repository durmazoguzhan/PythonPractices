# def sum(a,b):
#     return a+b

# def sum(a,b,c):
#     return a+b+c

# numbers=[5,25,15,30]

# def sum(numbers):
#     result=0
#     for number in numbers:
#         result+=number
#     return f"Sum of numbers : {result}"

# print(sum(numbers))

def sum(*args):
    result=0
    for number in args:
        result+=number
    return result

print(sum(5,10,3,2))