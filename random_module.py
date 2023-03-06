import random

result = dir(random)
result = random.random()  # random generate numbers between 0 and 1
result = int(random.random() * 10)
result=int(random.uniform(10,100)) # random select between 10 and 100
result=random.randint(0,50) # random generate int numbers between 0 and 50

users=["mehmet","selin","oguzhan","mechsoft","ahmet","ozgur","atakan","firat"]
name="oguzhan"

#result=users[random.randint(0,len(users)-1)]
result=random.choice(users)
result=random.choice(name)

list1=list(range(10))
random.shuffle(list1)

list2=list(range(100))
result=random.sample(list2,3)

result=random.sample(users,2)

print(result)