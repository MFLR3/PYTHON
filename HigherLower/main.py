import random
import game_data
import art

g_data = game_data
artwork = art
count = 0

def random_numbers_generator():
  num_1 = random.randint(1, len(g_data.data))
  num_2 = random.randint(1, len(g_data.data))
  while(num_1 == num_2):
    num_2 = random.randint(1, len(g_data.data))  
  return num_1, num_2

def next_round():
  num_1, num_2 = random_numbers_generator()
  print("Compare A: ", g_data.data[num_1]["name"],
        " a ", g_data.data[num_1]["description"], 
        " from ", g_data.data[num_1]["country"] + ".")
  print(artwork.vs)
  print("Against B: ", g_data.data[num_2]["name"],
        " a ", g_data.data[num_2]["description"], 
        " from ", g_data.data[num_2]["country"] + ".")  
  
  user_choice = input("Who has more followers? Type 'A' or 'B': ").upper()
  while user_choice != "A" and user_choice != "B":
    print()
    print("Please select 'A' or 'B'")
    user_choice = input("Who has more followers? Type 'A' or 'B': ").upper()

  if user_choice == "A":
    if g_data.data[num_1]["follower_count"] < g_data.data[num_2]["follower_count"]:
      return False
    elif g_data.data[num_1]["follower_count"] > g_data.data[num_2]["follower_count"]:
      return True
  elif user_choice == "B":
    if g_data.data[num_1]["follower_count"] < g_data.data[num_2]["follower_count"]:
      return True
    elif g_data.data[num_1]["follower_count"] > g_data.data[num_2]["follower_count"]:
      return False

print("Guess which has the most Instagram Followers")
print(artwork.logo)
  
isTrue = True
count = 0

while(isTrue):
  isTrue = next_round()
  
  if isTrue:
    count += 1
    print()
    print("You're correct! Current score: ", count)
    print()
    
print()
print("Sorry, that's wrong. Final score: ", count)

# All code in main.py written by Max Reinsch 2024
