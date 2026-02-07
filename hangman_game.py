import random
import string

WORDS = [
    "python", "developer", "hangman", "algorithm",
    "computer", "programming", "function", "variable",
    "keyboard", "internet"
]

def play_hangman():
    word = random.choice(WORDS)
    guessed = set()
    lives = 6

    print("\n🎮 Welcome to Hangman Game!")
    print("Guess the word, one letter at a time.")

    while lives > 0:
        display = " ".join([c if c in guessed else "_" for c in word])
        print("\nWord:", display)
        print("Lives:", lives)
        print("Guessed letters:", " ".join(sorted(guessed)))

        if "_" not in display:
            print("\n🎉 You WON! The word was:", word)
            return

        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or guess not in string.ascii_lowercase:
            print("❌ Enter only ONE letter.")
            continue

        if guess in guessed:
            print("⚠️ Already guessed.")
            continue

        guessed.add(guess)

        if guess not in word:
            lives -= 1
            print("❌ Wrong guess!")

    print("\n💀 Game Over! The word was:", word)


if __name__ == "__main__":
    play_hangman()
