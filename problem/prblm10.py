import random

def determine_winner(player, computer):
    if player == computer:
        return "It's a tie!"
    elif (player == "rock" and computer == "scissors") or \
         (player == "scissors" and computer == "paper") or \
         (player == "paper" and computer == "rock"):
        return "You win!"
    else:
        return "You lose!"

options = ["rock", "paper", "scissors"]
player_score = 0
computer_score = 0

while True:
    player_choice = input("Enter rock, paper, or scissors (or 'quit' to stop): ").lower()
    if player_choice == "quit":
        break
    if player_choice not in options:
        print("Invalid choice. Try again.")
        continue

    computer_choice = random.choice(options)
    print("Computer chose:", computer_choice)
    result = determine_winner(player_choice, computer_choice)
    print(result)

    if result == "You win!":
        player_score += 1
    elif result == "You lose!":
        computer_score += 1

    print(f"Score -> You: {player_score}, Computer: {computer_score}")
