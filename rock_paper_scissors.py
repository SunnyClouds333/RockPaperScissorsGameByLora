import random

rock = 'Rock'
paper = "Paper"
scissors = "Scissors"

player_choice = input("Choose: [r]ock, [p]aper or [s]cissors: ")

if player_choice == 'r':
    player_choice = rock
elif player_choice == 'p':
    player_choice = paper
elif player_choice == 's':
    player_choice = scissors
else:
    raise SystemExit("Invalid Input. Try again...")


computer_random_choice = random.randint(1, 3)
computer_choice = ''
if computer_random_choice == 1:
    computer_choice = rock
elif computer_random_choice == 2:
    computer_choice = paper
elif computer_random_choice == 3:
    computer_choice = scissors
print(f"The computer chose {computer_choice}.")

if player_choice == rock and computer_choice == scissors  or player_choice == paper and computer_choice == rock\
        or player_choice == scissors and computer_choice == paper:
    print("You win!")
elif player_choice == computer_choice:
    print("Draw!")
else:
    print("You lose!")

