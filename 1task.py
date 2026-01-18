import random

# List of predefined words
words = ["Python", "hangman", "intern", "coding", "project"]

# Select a random word
secret_word = random.choice(words)
guessed_letters = []
attempts = 6

print("🎮 Welcome to Hangman Game!")
print("Guess the word, one letter at a time.")

while attempts > 0:
    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word.strip())
    print("Remaining attempts:", attempts)

    # Check if player has won
    if "_" not in display_word:
        print("🎉 Congratulations! You guessed the word correctly!")
        break

    guess = input("Enter a letter: ").lower()

    if guess in guessed_letters:
        print("⚠️ You already guessed that letter.")
    elif guess in secret_word:
        print("✅ Correct guess!")
        guessed_letters.append(guess)
    else:
        print("❌ Wrong guess!")
        guessed_letters.append(guess)
        attempts -= 1

if attempts == 0:
    print("\n💀 Game Over! The word was:", secret_word)
