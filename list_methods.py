numbers=[3,5,10,67,27,27,27]
letters=["a","c","m","x","f","f","f"]

print(min(numbers))
print(max(numbers))

print(min(letters))
print(max(letters))

#add with append method - add item as last item
numbers.append(81)
print(numbers)
letters.append("i")
print(letters)

#add with insert method
numbers.insert(1,60)
print(numbers)
letters.insert(3,"o")
print(letters)

#delete
numbers.pop() #delete last item
print(numbers)

letters.pop() #delete last item
print(letters)

##remove - delete item by item value
numbers.remove(60)
print(numbers)
letters.remove("c")
print(letters)

# sorting

numbers.sort()
print(numbers)
letters.sort()
print(letters)

numbers.reverse() #reverse list items
print(numbers)

print(numbers.count(27))

#find index
print(numbers.index(10))

#clear the list
numbers.clear()
print(numbers)