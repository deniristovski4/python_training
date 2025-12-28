# EE -  Hangman Game

import random
word_list = ['python', 'java', 'kotlin', 'javascript', 'hangman', 'programming', 'developer', 'challenge', 'function', 'variable', 'condition', 'loop', 'string', 'integer', 'boolean', 'dictionary', 'list', 'tuple', 'set', 'exception', 'module']
secret_word = random.choice(word_list)
guessed_letters = set()
attempts = 6
word_completion = ['_'] * len(secret_word)

print("Welcome to Hangman!")

while attempts > 0 and "_" in word_completion:
    print("\n" + " ".join(word_completion))
    print(f"You have {attempts} attempts left.")
    guess = input("Guess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single alphabetical character.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue
    guessed_letters.add(guess)
    if guess in secret_word:
        for index, letter in enumerate(secret_word):
            if letter == guess:
                word_completion[index] = guess
        print("Good guess!")
    else:
        attempts -= 1
        print("Wrong guess.")

if "_" not in word_completion:
    print(f"\nCongratulations! You guessed the word: {secret_word}")
else:
    print(f"\nSorry, you ran out of attempts. The word was: {secret_word}")