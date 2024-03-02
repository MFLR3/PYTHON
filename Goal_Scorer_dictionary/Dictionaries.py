#Dictionary example
# Top Goalscorers 2023
goals_scored = {
  "Cristiano Ronaldo": 53,
  "Harry Kane": 52,
  "Kylian Mbappe": 52, 
  "Erling Haaland": 50,
  "German Cano": 40,
}

player_status = {}

for goal in goals_scored:
  if goals_scored[goal] == 53:
    status = "Number 1 goal scorer"
  elif goals_scored[goal] == 52:
    status = "Number 2 goal scorer"
  elif goals_scored[goal] == 52:
    status = "Number 3 goal scorer"
  elif goals_scored[goal] == 50:
    status = "Number 4 goal scorer"
  elif goals_scored[goal] == 40:
    status = "Number 5 goal scorer" 
  player_status[goal] = status
  
print(player_status)
