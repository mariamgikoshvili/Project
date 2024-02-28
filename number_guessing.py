
import random
def check_answer(guess, answer, turns, num_guessed):
    if guess not in num_guessed:
        if guess > answer:
            print(f"The number is less than {guess}")
            num_guessed.append(guess)
            return turns - 1
        elif guess < answer:
            print(f"The number is more than {guess}")
            num_guessed.append(guess)
            return turns - 1
        else:
            print(f"Congratulations! The answer was {answer}.")
    else:
        print(f"You have already chosen number {guess},Choose different number: ")
        return turns
def ask_input():
    while True:
        try:
            guess = int(input("Make a guess! "))
            if guess in range(1,100):
                return guess
                break
            else:
                print("Choose number between 1 and 100!")
        except ValueError:
            print("You can only enter a number!")


def game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = random.randint(1,100)
    guess = 0
    turns = 7
    num_guessed = []
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        guess = ask_input()
        turns = check_answer(guess, answer, turns, num_guessed)
        if turns == 0:
            print("You've run out of guesses, you lose.")
            break
        elif guess != answer:
            print("guess again")
def play_game():
    game()
    while True:
        cont = input("Would you like to play the game again? Type 'yes' or 'no': ").lower()
        if cont == 'yes':
            game()
        elif cont == 'no':
            print("Thanks for playing! Goodbye!")
            break
        else:
            print("Please type 'yes' or 'no'! ")


play_game()