import time
import random
Choice = input("Rock, Paper or scissors: ")
Choice2 = random.randint(1, 3)

if Choice == ("rock") or (Choice == "Rock"):
    Choice = "🗿"
elif Choice == ("paper") or (Choice == "Paper"):
    Choice = "📄"
elif Choice == ("scissors") or (Choice == "Scissors"):
    Choice = "✂️"
else:
    print("Say Rock, Paper or Scissors")

if Choice2 == 1:
    Choice2 = "🗿"
elif Choice2 == 2:
    Choice2 = "📄"
elif Choice2 == 3:
    Choice2 = "✂️"

print("Rock...")
time.sleep(0.5)
print("Paper...")
time.sleep(0.5)
print("Scissor...")
time.sleep(0.5)
print("Shoot!")
print("-----------------")
print("You       Opponent")
print(Choice,"      ", Choice2)


if Choice == Choice2:
    print("Tie!")
