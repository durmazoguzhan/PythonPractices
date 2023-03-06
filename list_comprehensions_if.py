
evenNumbers=[a for a in range(20) if a%2==0]
oddNumbers=[a for a in range(20) if a%2!=0]
# print(evenNumbers)
# print(oddNumbers)

numbers=[f"{number}-even" if number%2==0 else f"{number}-odd" for number in range(10)]
print(numbers)