# a=10
# b=10
# c=10

# a,b,c=10,20,30

# a,b=b,a

# a=a+5
# a+=5
# a-=5

numbers=(1,2,3,4,5,6)
a,b,*c=numbers
print(a,b,c)
a,*b,c=numbers
print(a,b,c)
*a,b,c=numbers
print(a,b,c)