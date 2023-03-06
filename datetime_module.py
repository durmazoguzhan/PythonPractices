# import datetime

from datetime import datetime
from datetime import timedelta
# from datetime import date
# from datetime import time

#result=dir(datetime)
nowDateTime=datetime.now()
nowDateTime=datetime.today()
#print(type(nowDateTime))
result=nowDateTime.year
result=nowDateTime.month

result=datetime.ctime(nowDateTime)
result=datetime.strftime(nowDateTime,"%Y")
result=datetime.strftime(nowDateTime,"%X")
result=datetime.strftime(nowDateTime,"%A")
result=datetime.strftime(nowDateTime,"%w %B") #https://www.w3schools.com/python/python_datetime.asp


birthday=datetime(2000,9,11,9,0,50)
result=datetime.timestamp(birthday)
result=datetime.now()-birthday
result=result.seconds
result=datetime.now()+timedelta(365)
result=datetime.now()+timedelta(days=365,minutes=20)
result=datetime.now()-timedelta(days=365,minutes=20)


print(result)