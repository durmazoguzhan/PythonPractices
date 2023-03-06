import module

result=module.password
result=module.numbers[0]
result=module.user
result=module.user["username"]
result=module.user["scores"]
result=module.average(100,50)

import module as md1

result=md1.numbers

from module import user,average

result=user
result=average(200,300)

from module import *

result=password

print(result)