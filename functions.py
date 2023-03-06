def printHelloWorld():
    print("Hello World!")


def sumNumbers(a, b):
    print(a+b)


def sayHi():
    return "hi"


def findLettersCount(text, wantedLetter):
    count = 0
    for letter in text:
        if (letter == wantedLetter):
            count += 1
    return count

def calculateAge(year):
    return 2023-year


# printHelloWorld()
# sumNumbers(3,5)
# print(sayHi())
text = "Oguzhan Durmaz"
letter="b"
count=findLettersCount(text,letter)
print(f"{letter} letter count: {count}")

for i in range(5):
    printHelloWorld()
    
print(calculateAge(1973))