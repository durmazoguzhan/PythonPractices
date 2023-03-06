import os
print()

# result=os.name

# # getting current path
# result=os.getcwd()

# changing path
# result=os.chdir("..")
# result=os.chdir("..")
#result=os.chdir("../..")

# result=os.chdir("\\Users")
# result=os.getcwd()

# create folder
#os.mkdir("new_folder")
#os.makedirs("new_folder/test_folder/another_folder")
#os.rename("new_folder","newer_folder")
#os.removedirs("newer_folder/test/another_folder")

# list folders
# result=os.listdir("\\Users")
# for file in os.listdir():
#     if(file.endswith(".py")):
#         print(file)


result=os.stat("args.py")
result=result.st_size / 1024


print(result)
print()