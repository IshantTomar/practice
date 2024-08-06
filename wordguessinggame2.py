import random

words = ["apple", "mango", "banana"]
selected = random.choice(words)
chance = 3
right = ""
guessed_characters = []

while chance > 0:
    wrong = 0
    guessed_characters = []

    for char in selected:
        if char in right:
            guessed_characters.append(char)
        else:
            guessed_characters.append("_")

    print(" ".join(guessed_characters))

    if "_" not in guessed_characters:
        print(f"Correct! The word is {selected}.")
        break

    guess = input("Make a Guess: ").lower()

    if guess in selected:
        if guess not in right:
            right += guess
    else:
        chance -= 1
        print(f"Wrong! You have {chance} chances left.")

if chance == 0:
    print(f"Out of chances! The word was {selected}.")
