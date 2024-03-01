# Cipher Program
## Variables
- alphabet
- direction
- text
- shift
- ciphered_word
- index
- processed_word

## Functions
### Cipher
- Takes 3 arguments:
  - direction - stored input for choice between encoding and decoding.
  - text - stored input for text to be encoded or decoded.
  - shift - stored input for number of spaces.
- If direction == "encode":
  - For every letter text variable:
    - If letter in alphabet, get index value of letter from alphabet list.
    - If letter index + shift is more than length of alphabet list, deduct length of alphabet from index value when assigning new letter to 'ciphered_word'.
    - Else if index + shift is less then length of alphabet list, assign 'alphabet[index + shift]' to 'ciphered_word'.
   
- If direction == "decode":
    - For every letter text variable:
      - If letter in alphabet, get index value of letter from alphabet list.
      - Assign 'alphabet[index - shift]' to 'ciphered_word'.

- Return 'ciphered_word'.

## Main
- Prompt user input for 'direction', 'text' and 'shift' variables.
- Pass 'direction', 'text' and 'shift' variables as arguments into 'cipher' function, assign returned value into 'processed_word' variable.
- Print results.
