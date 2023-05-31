import random

word_list = ['hello', "bastard", "squire", "courtesy", "knight", "traitor", "savage"]

def play_game():
    word = random.choice(word_list)
    guess_result = '?' * len(word)
    guessed_letters = []
    entered_letters = set()
    counter = 5

    available_letters = 'abcdefghijklmnopqrstyuwxvz'

    while guess_result != word and counter > 0:

        print(f'Guess the word: {guess_result}')

        while True:
            user_letter = input('Enter the letter: ').lower()
            if len(user_letter) != 1:
                print('Too long or too short!')
                print("Remaining attempts:", counter)
                continue
            elif user_letter not in available_letters:
                print('Unavailable!')
                print("Remaining attempts:", counter)
                continue
            elif user_letter in entered_letters:
                print('Duplicate!')
                print("Remaining attempts:", counter)
                continue


            entered_letters.add(user_letter)
            break


        if user_letter in word:
            guessed_letters.append(user_letter)
            guess_result = ''.join(['?' if char not in guessed_letters else char for char in word])
            print("Remaining attempts:", counter)
        else:
            counter -= 1
            print('Incorrect! Try again!')
            print("Remaining attempts:", counter)

    if not '?' in guess_result:
        print('Congratulations!')
    elif counter == 0:
        print("Attempts are over")

    print(f'The word was: {word}')

play_game()
while True:
    user_input = input("Do you want to play again? (yes/no): ").lower()

    if user_input == "yes":
        play_game()
    elif user_input == "no":
        print("Okay. Goodbye!")
        exit()
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")