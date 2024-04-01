import time
import random
Bob = 0
Trys = 0

while Bob == 0: 
    time.sleep(0)
    Trys = Trys + 1
    Number = str(random.randint(1, 2))
    print(Number, Trys)
    if Number == 2:
        break
print("finished")
