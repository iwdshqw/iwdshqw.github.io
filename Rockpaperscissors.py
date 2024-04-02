import time
Choice = input("Rock, Paper or scissors: ")

if Choice == "rock" or "Rock":
    Choice = 1
    print(Choice)
elif Choice == "paper" or "Paper":
    Choice = 2
    print(Choice)
elif Choice == "scissors" or "Scissors":
    Choice = 3
    print(Choice)
else:
    print("Say Rock, Paper or Scissors")
