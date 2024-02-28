import random
word_list=['cat','flu','follow','discovery','virtue','banana','season','level','production','game','dress']
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

def ask_input(letters_guessed,word_length):
    while True:
        print(f'You have used letters: {letters_guessed}.')
        guess = input("Guess a letter: ")
        if (len(guess) == word_length or len(guess) == 1) and guess.isalpha():
            if guess in letters_guessed:
                print(f'You have already guessed {guess}. Choose different letter.')
            else:
                return guess.lower()
        else:
            print("You can only enter one letter or the whole word!")
def game():
    chosen_word = random.choice(word_list)
    word_length = len(chosen_word)
    letters_guessed = []
    lives = 6
    display = []
    print("Welcome to the Hangman Game!")
    print("You have 6 lives to guess the word")
    for _ in range(word_length):
        display += "_"
    print(f"{' '.join(display)}")
    while True:
        guess = ask_input(letters_guessed,word_length)
        letters_guessed.append(guess)
        for position in range(word_length):
            letter = chosen_word[position]
            if letter == guess:
                display[position] = letter
        if len(guess) != 1:
            if guess == chosen_word:
                print("Congrats! You have guessed the word!")
                break
            else:
                print("This is not a word. guess again")
                lives -= 1
                print(f'You have {lives} lives left.')
        elif guess not in chosen_word:
            lives -= 1
            print(f"You guessed {guess}, that's not in the word. You lose a life.")
            print(f'You have {lives} lives left.')
            if lives == 0:
                print("Sorry, You lose.")
                print(stages[lives])
                break
        print(f"{' '.join(display)}")
        if "_" not in display:
            print("Congrats! You won.")
            break
        print(stages[lives])

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
