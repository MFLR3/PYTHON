#Password Generator
import random

letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "!#$%&()*+"

print("Password Generator")
num_letters= int(input("How many letters would you like in your password?\n")) 
num_symbols = int(input("How many symbols would you like?\n> "))
num_numbers = int(input("How many numbers would you like?\n> "))

password_length = num_symbols + num_numbers + num_letters
print(password_length)
password_list = []
password_as_string = ""

for i in range(0, num_letters):
  password_list.append(random.choice(letters))
for i in range(0, num_symbols):
  password_list.append(random.choice(symbols))
for i in range(0, num_numbers):
  password_list.append(random.choice(numbers))

random.shuffle(password_list)

for p in password_list:
  password_as_string += p
  
print(password_as_string)
