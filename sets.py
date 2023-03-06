#list       -> list
#tuple      -> const list
#dictionary -> key-value
#sets       -> const list, non-sortable, non-indexing and best performance

brands={"Audi","Mercedes-Benz","Honda","BMW"}
brands2={"Suzuki","Jaguar","Fiat"}

print(brands)
#print(brands[0]) #type error

print("Honda"in brands)

brands.add("Renault")
print(brands)
brands.update(["Opel","Toyota","Seat"])
print(brands)

brands.remove("Opel")
print(brands)

brands.pop()
print(brands)

#brands.clear()
#print(brands)

resultSets=brands.union(brands2)
print(resultSets)