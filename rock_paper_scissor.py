import random
computer_choice = random.choice(["scissors", "rock", "paper"])

user_choice = input("do you want - rock, paper, or scissors?\n")

if computer_choice == user_choice:
    print("tie")
elif user_choice == "rock" and computer_choice == "scissors":
    print("you win")
elif user_choice == "paper" and computer_choice == "rock":
    print("you win")
else:
    print(f"you lose, computer chose {computer_choice} and wins!")