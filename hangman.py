import random


def choose_word():
    words = [
        "python",
        "hangman",
        "computer",
        "programming",
        "gaming",
        "elephant",
        "banana",
        "chocolate",
    ]
    return random.choice(words)


def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display


def hangman():
    word = choose_word()
    max_attempts = 6
    attempts = 0
    guessed_letters = set()

    print("Welcome to Hangman!")
    while True:
        print("\n", display_word(word, guessed_letters))

        if "_" not in display_word(word, guessed_letters):
            print("Congratulations! You guessed the word:", word)
            break

        guess = input("Enter a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
        elif guess in word:
            guessed_letters.add(guess)
        else:
            print("Incorrect guess.")
            attempts += 1

        if attempts >= max_attempts:
            print("You ran out of attempts. The word was:", word)
            break


# main
hangman()
