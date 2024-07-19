import random

words = ["apple", "mango", "banana"]
selected = random.choice(words)
chance = 3
right = ""
while chance > 0:
    wrong = 0
    for char in selected:
        if char in right:
            print(char, end="")
        else:
            print("_", end=" ")
            wrong += 1

    if wrong == 0:
        print(f"Correct! The word is {selected}.")
        break
    guess = input("\n Make a Guess: ")
    right += guess

    if guess not in selected:
        chance -= 1

        if chance == 0:
            print(selected)
            print(";(")