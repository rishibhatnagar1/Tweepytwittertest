import time
import datetime
import math
before = datetime.datetime.now()
time.sleep(10)
after = datetime.datetime.now()
mins  = math.floor((after - before).seconds)
print (mins) 
