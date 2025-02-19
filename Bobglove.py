import time
import random
Bob = 0
Trys = 0
Time = 0

while Bob == 0: 
    time.sleep(0) #sets the amount of time before looping
    Time = Time + 14
    Trys = Trys + 1
    Number = random.randint(1, 7500)
    print(Number,"Trys:",Trys,"Time(s):",Time)
    if Number == 7500:
        break
print("finished")
