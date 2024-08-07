# Us states guessing game
## Concept taken from the '100 Days of Code: The Complete Python Pro Bootcamp' by Angela Yu on Udemy. - https://www.udemy.com/course/100-days-of-code

main.py is entirely my attempt at the challenge, without looking at the solution. 

All files excluding main.py are taken from the '100 Days of Code: The Complete Python Pro Bootcamp' and are not my code. 

This is based on the quiz game taken from: https://www.sporcle.com/games/g/states

### Performs the following:

1. Updates amount of correct answers in the text input window.
2. Prompts user for a US state
3. Capitalises the user guess using title method.
4. If user guess is in 50_states.csv file and not in correct_guesses list:
- appends user guess to correct_guesses list
- gets x and y values for correct US state from 50_states.csv
- Converts x and y values into Int data type and create position tuple
- Creates Turtle object for writing
- Using Turtle object, writes correct US state using position tuple.
- Adds 1 to correct_answers_amount 

### Potential updates
1. Add a success window
2. Add a timer for added challenge.
