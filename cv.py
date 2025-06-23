import random

with open("common_words.txt", "r") as file:
    word_list = [line.strip().lower() for line in file if line.strip().isalpha() and len(line.strip()) == 7]

chosen_word = list(random.choice(word_list))
wordle_array = ["_"] * len(chosen_word)

print("Welcome to wordle")
attempt = 10

while "_" in wordle_array:
    chosen_letter = input("ENTER YOUR CHOSEN LETTER IN LOWER CASE: ").lower()

    if chosen_letter.isalpha() and len(chosen_letter) == 1:
        if chosen_letter in wordle_array:
            print(f"⚠️ You already revealed '{chosen_letter}' — try another letter.")
            continue

        found = False
        for i, letter in enumerate(chosen_word):
            if chosen_letter == letter:
                wordle_array[i] = chosen_letter
                found = True

        if found:
            print(f"✅ Good guess! '{chosen_letter}' is in the word.")
        else:
            attempt -= 1
            print(f"❌ Sorry, '{chosen_letter}' is not in the word.")
            print(f"Total guesses left: {attempt}")

        print("Word:", " ".join(wordle_array))

        if wordle_array == chosen_word:
            print("🎉 Congratulations on finishing the game!")
            break

        if attempt == 0:
            print("😢 Sorry, you lost!")
            break
    else:
        print("⚠️ Please enter a valid lowercase letter from a to z.")

print("Here is the actual word:", "".join(chosen_word))