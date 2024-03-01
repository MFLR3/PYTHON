# Cipher program
alphabet = "abcdefghijklmnopqrstuvwxyz"

# function
def cipher(direction, text, shift):
    ciphered_word = ""
    if(direction == "encode"):        
        for t in text:
            if t in alphabet:              
              index = alphabet.index(t)
              if alphabet.index(t) + shift > 25:
                ciphered_word += alphabet[index + shift - len(alphabet)]  
              else:
                ciphered_word += alphabet[index + shift]      
    elif(direction == "decode"):          
          for t in text:
            if t in alphabet:
              index = alphabet.index(t)
              ciphered_word += alphabet[index - shift]
    return ciphered_word 

# main
print("Please select an option: ")
direction = input("'encode' to encrypt, 'decode' to decrypt:\n> ")

while(direction != "encode" and direction != "decode"):
    print("Invalid input. Please try again.")
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n> ")

text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))   

processed_word = cipher(direction, text, shift)
print(f"The word {text} has been {direction}d to the following: ")
print(processed_word)
