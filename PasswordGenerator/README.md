# Password Generator

## Variables:
- letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
- numbers = "0123456789"
- symbols = "!#$%&()*+"
- num_letters= int(input("How many letters would you like in your password?\n")) 
- num_symbols = int(input("How many symbols would you like?\n> "))
- num_numbers = int(input("How many numbers would you like?\n> "))
- password_length = num_symbols + num_numbers + num_letters
- password_list = []
- password_as_string = ""

## Functionality
- Takes user-input for number of letters, numbers and symbols.
- Store length of password using user-input into "password_length" variable.
- Use for loops to randomly append all user input into "password_list" from the "letters", "numbers" and "symbols" strings.
- Randomly shuffle contents of "password_list" using "random.shuffle" method.
- Loop through shuffled "password_list" and concatenate all elements to build "password_as_string".
- Print Password

### Note: 
Idea for password generator taken from "100 Days of Code: The Complete Python Pro Bootcamp"
Link: https://www.udemy.com/course/100-days-of-code
All code is my attempt at the challenge.
