import random

def get_user_choice():
    while True:
        user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
        if user_choice in ["rock", "paper", "scissors"]:
            return user_choice
        else:
            print("Invalid choice. Please try again.")

def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        return "You win!"
    else:
        return "Computer wins!"

def play_game():
    score = {"You": 0, "Computer": 0}
    round = 1
    print("Welcome to Rock Paper Scissors!")
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        print(f"You chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")
        winner = determine_winner(user_choice, computer_choice)
        """If user wins, add 1 to user's score."""
        """If computer wins, add 1 to computer's score."""
        """If it's a tie, don't add anything to either score."""
        if winner == "You win!":
            score["You"] += 1
        elif winner == "Computer wins!":
            score["Computer"] += 1
        print(winner)
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            break
        round += 1
    """Print out the final scores."""
    print("Final scores:")
    print(f"You: {score['You']}")
    print(f"Computer: {score['Computer']}")
    print(f"Rounds played: {round}")
    print("Thanks for playing!")

play_game()
