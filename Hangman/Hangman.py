# Hangman game
import random
words = [
    "apple", "banana", "cat", "dog", "elephant", "fish", "grape", "house", 
    "iguana", "jacket", "kiwi", "lion", "monkey", "nut", "orange", "pear", 
    "queen", "rabbit", "snake", "tiger", "umbrella", "vase", "watermelon", 
    "xylophone", "yak", "zebra"
]

gallows = ["+---+\n" +
            "|   |\n" +
            "    |\n" +
            "    |\n" +
            "    |\n" +
            "    |\n" +
            "=========\n",

            "+---+\n" +
                    "|   |\n" +
                    "O   |\n" +
                    "    |\n" +
                    "    |\n" +
                    "    |\n" +
                    "=========\n",

            "+---+\n" +
                    "|   |\n" +
                    "O   |\n" +
                    "|   |\n" +
                    "    |\n" +
                    "    |\n" +
                    "=========\n",

            " +---+\n" +
                    " |   |\n" +
                    " O   |\n" +
                    "/|   |\n" +
                    "     |\n" +
                    "     |\n" +
                    " =========\n",

            " +---+\n" +
                    " |   |\n" +
                    " O   |\n" +
                    "/|\\  |\n" + 
                    "     |\n" +
                    "     |\n" +
                    " =========\n",

            " +---+\n" +
                    " |   |\n" +
                    " O   |\n" +
                    "/|\\  |\n" +
                    "/    |\n" +
                    "     |\n" +
                    " =========\n",

            " +---+\n" +
                    " |   |\n" +
                    " O   |\n" +
                    "/|\\  |\n" +
                    "/ \\  |\n" +
                    "     |\n" +
                    " =========\n"]

print("Welcome to the Hangman game")
secret_word_str = words[random.randint(0, len(words) - 1)]
secret_word = list(secret_word_str)
guessed_letters = []
errors = 0;

while(errors < 7):
    construct = ""
    current_guess = input("Guess a letter > ")

    while(len(current_guess) != 1 or current_guess.isnumeric() == True):
        print("Please input a letter" )
        current_guess = input("Guess a letter > ")

    if(current_guess in secret_word):
        if(current_guess not in guessed_letters):
            print("Correct!")
            guessed_letters.append(current_guess)
    else:
        print("Wrong!")
        print(gallows[errors])
        print("errors: " + str(errors))
        errors +=1

    for s in secret_word:
        if s in guessed_letters:
            construct += s
        else:
            construct += "_ "
            
    print("Word so far: " + construct)
    print("")
    print("")
    if(len(guessed_letters) == len(set(secret_word))):
        break    
      
if(len(guessed_letters) == len(set(secret_word))):
    print(f"Congratulations, you guessed {secret_word_str} correctly")
elif(errors == 7):
    print("Sorry, you lose!")
    print(gallows[-1])
    print(" ")
    print(f"Secret word was {secret_word_str}")
