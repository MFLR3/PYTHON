import random

def deal_card():
  random_number = random.randint(0, len(card_keys) - 1)
  return card_keys[random_number]  

cards = {
  "A": 11,
  "2": 2,
  "3": 3,
  "4": 4,
  "5": 5,
  "6": 6,
  "7": 7,
  "8": 8,
  "9": 9,
  "10": 10,
  "J": 10,
  "Q": 10,
  "K": 10,
}

card_keys = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
player_score = 0
dealer_score = 0

selected_player_cards = []
selected_dealer_cards = []

playing = True
hit = ""

while (playing == True):
  # Dealer Cards
  selected_dealer_cards.append(deal_card())
  selected_dealer_cards.append(deal_card())
  # Get total dealer score
  for card in selected_dealer_cards:  
    dealer_score += cards[card]
  # Player cards
  delt_card = deal_card()
  selected_player_cards.append(delt_card)
  player_score += cards[delt_card]
  
  while(player_score < 21):
    print(f"Dealers cards: ['-', '{selected_dealer_cards[-1]}']")
    print("Players Cards: ", selected_player_cards)
    print("Score: ", player_score)

    print()
    hit = input("'y' for another card, 'n' to pass > ")
    print()
    if(hit == "y"):
      delt_card = deal_card()
      selected_player_cards.append(delt_card)
      player_score += cards[delt_card]
      print()
      
      if(player_score > 21):
        print("Player Score: ", player_score)
        print("You Lose")
        playing = False
        break        
        
    elif(hit == "n"):
      print("Dealers Cards: ", selected_dealer_cards)
      print("Dealer Score: ", dealer_score)
      print()
      print("Players Cards: ", selected_player_cards)
      print("Player Score: ", player_score)
      print()

      if(player_score < dealer_score):
        print("You lose!")
      elif(player_score > dealer_score):
        print("You win!!")
      elif(player_score == dealer_score):
        print("It's a draw!!")      

      input("Enter anything to exit game.")
      playing = False
      break
