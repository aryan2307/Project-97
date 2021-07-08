import random
turn = 0
winner = "no"
number = int(input("enter any number between 1 and 9"))
rand = random.randint(1,9)
while turn<4 and winner == "no":
    if number==rand:
      print("Congratulations! You guessed the number")
      winner="yes"
      turn+=1
    elif number>rand:
      print("You guessed high! Try again.")
      number = int(input("enter any number between 1 and 9"))
      turn+=1
    elif number<rand:
      print("You guessed low! Try again.")
      number = int(input("enter any number between 1 and 9"))
      turn+=1
if winner=="no":
    print("You lost!")