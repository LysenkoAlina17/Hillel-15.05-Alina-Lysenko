#Напишіть декоратор, який вимірює час виконання функції. робота з часом в python -  import time
import time
def measure_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Функція {func.__name__} виконалася за {execution_time} секунд")
        return result
    return wrapper

#Задекоруйте цим декоратором вашу гру з попереднього домашнього завдання
import time
import random

choices = ["rock", "paper", "scissors"]
def measure_time (func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Функція {func.__name__} виконалася за {execution_time} секунд")
        return result
    return wrapper

@measure_time
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

@measure_time
def get_computer_choice():
    """
    Функція генерує рандомний вибір комп'ютера та повертає його
    """
    return random.choice(choices)


@measure_time
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

@measure_time
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


@measure_time
def play_again():
    """Функція визначає чи хоче гравець зіграти знову та у випадку відповіді "так" починає гру спочатку """
    while True:
        user_input = input("Do you want to play again? (yes/no): ").lower()

        if user_input == "yes":
            play_game()
        elif user_input == "no":
            print("Okay. Goodbye!")
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

play_game()
play_again()

