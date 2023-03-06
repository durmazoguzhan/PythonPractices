# num=int(input("please enter a number: "))
# if(num>0):
#     if(num%2==0):
#         print(f"{num} is positive and even")
#     else:
#         print(f"{num} is positive and odd")
# elif(num<0):
#     if(num%2==0):
#         print(f"{num} is negative and even")
#     else:
#         print(f"{num} is negative and odd")
# else:
#     print(f"{num} is neutral and even")


# ## repeat same line shift+alt+down arrown
# num1=int(input("num1 : "))
# num2=int(input("num2 : "))
# num3=int(input("num3 : "))

# if(num1>num2 and num1>num3):
#     print(f"{num1} is biggest number.")
# elif(num2>num1 and num2>num3):
#     print(f"{num2} is biggest number.")
# elif(num3>num1 and num3>num2):
#     print(f"{num3} is biggest number.")
# else:
#     print("numbers are equal.")

name=input("name : ")
age=int(input("age : "))
education=input("education : ")

if(age>=18):
    if(education=="high school"or education=="university"):
        print(f"{name} can take driving license.")
    else:
        print(f"{name} can't take driving license, because education level is not enough.")
else:
    print(f"{name} can't take driving license, because age is younger than 18.")