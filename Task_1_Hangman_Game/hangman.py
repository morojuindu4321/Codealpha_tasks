import random

WORDS = ["python", "guess", "hangman", "random", "string"]

def play_game():
    secret_word = random.choice(WORDS)
    guessed_letters = []
    wrong_guesses = 0

    while wrong_guesses < 6:
        display = ""
        for letter in secret_word:
            if letter in guessed_letters:
                display += letter + " "
            else:
                display += "_ "

        print("\nWord:", display)
        print("Guessed Letters:", guessed_letters)
        print("Wrong Guesses Left:", 6 - wrong_guesses)

        if "_" not in display:
            print(f"\nCongratulations! You guessed the word: {secret_word}")
            return

        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Enter one letter only.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess not in secret_word:
            wrong_guesses += 1
            print("Incorrect guess!")

    print(f"\nGame Over! The word was: {secret_word}")

def main():
    while True:
        play_game()
        replay = input("Play again? (yes/no): ").lower()
        if replay not in ["yes", "y"]:
            break

if __name__ == "__main__":
    main()
