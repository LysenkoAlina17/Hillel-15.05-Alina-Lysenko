import random

choices = ["rock", "paper", "scissors"]
def get_player_choice():
    """
    Функція запитує вибір гравця (камінь, ножиці, папір) і повертає його.
    """
    while True:
        player_choice = input("Enter your choice (rock, paper, scissors):").lower()
        if player_choice in choices:
            return player_choice
        else:
            print("Incorrect choice. Try again.")
def get_computer_choice():
    """
    Функція генерує рандомний вибір комп'ютера та повертає його
    """
    return random.choice(choices)

def determine_winner(player_choice, computer_choice):
    """
    Функція визначає переможця гри залежно від виборів гравця і комп'ютера.
    Повертає "player" у разі перемоги гравця, "computer" у разі перемоги комп'ютера, або "tie" у разі нічиєї.
    """
    if player_choice == computer_choice:
        return "tie"
    elif (player_choice == "rock" and computer_choice == "scissors") or \
            (player_choice == "paper" and computer_choice == "rock") or \
            (player_choice == "scissors" and computer_choice == "paper"):
        return "player"
    else:
        return "computer"

def play_game():
    """
    Функція безпосердньо для гри 'Rock paper scissors'
    """
    print("Game 'Rock paper scissors'!")
    player_choice = get_player_choice()
    computer_choice = get_computer_choice()
    print(f"Player: {player_choice}")
    print(f"Computer: {computer_choice}")
    winner = determine_winner(player_choice, computer_choice)
    if winner == "tie":
        print("Tie!")
    else:
        print(f"Winner: {winner}!")



play_game()
while True:
    user_input = input("Do you want to play again? (yes/no): ").lower()

    if user_input == "yes":
        play_game()
    elif user_input == "no":
        print("Okay. Goodbye!")
        break
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")