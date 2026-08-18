import random

def play_hangman():
    words = ["python", "keyboard", "monitor", "variable", "developer"]

    word = random.choice(words)
    guessed_letters = []
    attempts = 6

    print("Welcome to Hangman!")
    print(f"You have {attempts} incorrect guesses. Good luck!\n")

    while attempts > 0:
        display_word = ""

        for letter in word:
            if letter in guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "

        print(f"Word: {display_word.strip()}")
        print(f"Incorrect guesses left: {attempts}")

        if "_" not in display_word:
            print("\nCongratulations! You guessed the word!")
            break

        guess = input("Guess a letter: ").lower()
        print("-" * 30)

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print(f"Good job! '{guess}' is in the word.")
        else:
            attempts -= 1
            print(f"Sorry! '{guess}' is not in the word.")

    if attempts == 0:
        print("\nGame Over! You've run out of guesses.")
        print(f"The correct word was: '{word}'")


if __name__ == "__main__":
    play_hangman()