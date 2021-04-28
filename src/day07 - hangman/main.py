import random
import hangman_art
import hangman_words

categories = hangman_words.categories
word_list = []
display = []
guessed_letters = []
lives = 6
end_of_game = False

print(hangman_art.logo)
print("\n")

print("Choose a category (Type de corresponding number):")
for i in range(0, len(categories)):
    print(f"{i+1} - {categories[i]}")
category = int(input()) - 1

if category < 0 or category > 3:
    print("You typed an invalid number!")
    print("The category is going to be choosen randomly...")
    category = random.randint(0,0)
    print("\n")

print(f"The choosen category is {categories[category]}.\n")

if category == 0:
    word_list = hangman_words.fruits
elif category == 1:
    word_list = hangman_words.animals
elif category == 2:
    word_list = hangman_words.countries
    
random_word = random.choice(word_list)

#print(f"Psssst, the chosen word is {random_word}.")

for blank in random_word:
    if blank == " ":
        display.append(" ")
    else:
        display.append("_")

print(f"\n{' '.join(display)}\n")

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in guessed_letters:
        print(f"You've already guessed the letter {guess}!")
    else:
        guessed_letters.append(guess)

        if guess in random_word:
            for i in range(len(random_word)):
                if random_word[i] == guess:
                    display[i] = random_word[i]
                    is_right_guess = True
        else:
            print(f"You guessed {guess}, it's not in the word... You lose a life!")
            lives -= 1   

    print(f"{' '.join(display)}")
    print(hangman_art.stages[lives])

    if "_" not in display:
        end_of_game = True
        print("You Win!")

    if not lives:
        end_of_game = True
        print("You lose!")
        print(f"The word was {random_word}")