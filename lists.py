import random

choices = ["rock", "paper", "scissors"]

def get_winner(player, computer):
    if player == computer:
        return "draw"
    elif (player == "rock" and computer == "scissors") or \
         (player == "paper" and computer == "rock") or \
         (player == "scissors" and computer == "paper"):
        return "win"
    else:
        return "lose"

print("🎮 Rock, Paper, Scissors Game!")
print("Type 'rock', 'paper', or 'scissors' (or 'q' to quit)\n")

while True:
    player = input("Your choice: ").lower()

    if player == "q":
        print("Goodbye!")
        break

    if player not in choices:
        print("Invalid choice, try again.\n")
        continue

    computer = random.choice(choices)
    print(f"Computer chose: {computer}")

    result = get_winner(player, computer)

    if result == "draw":
        print("It's a draw!\n")
    elif result == "win":
        print("You win! 🎉\n")
    else:
        print("You lose! 😢\n")
        
print("Thanks for playing!")
