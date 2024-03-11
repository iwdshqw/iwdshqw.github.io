import random
import time
Score = 0
Number = (random.randint(0, 1))
Guess = int(input())

if (Guess == Number):
    print("Yes")
    Score = Score + 1
    print(Score)
#Guess the number game
