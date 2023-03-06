programmingLanguages=["Python","Java","Kotlin"]

# for language in programmingLanguages:
#     print(language)
    
# enumerate method

# enumObject=enumerate(programmingLanguages)

for language in enumerate(programmingLanguages):
    print(language)

for index,language in enumerate(programmingLanguages):
    print(f"{index+1} - {language}")