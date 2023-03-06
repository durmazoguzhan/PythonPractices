numbers = [3, 5, 2, 9, 13, 56, 24, 38, 72, 14]
letters = ['a', 'b', 'c', 'o', 'd', 'm', 'l']
names = ["oguzhan", "durmaz", "ozgur", "atakan", "gurhan"]

result = min(numbers)
result = max(numbers)

result = min(letters)
result = max(letters)

result = min(names)
result = max(names)

result = [len(name) for name in names]
result = max([len(name) for name in names])

result = max(names, key=lambda n: len(n))
result = min(names, key=lambda n: len(n))


print(result)