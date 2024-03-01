# Prime number checker
def prime_number_checker(number):
  count = 0
  for n in range(1, (number + 1)):
    if(number % n == 0):
      count += 1
  if(count == 2):
    print("Prime.")
  else:
    print("Not Prime.")

# In range of 100
for i in range(1, 101):
    print(i, end=" ")
    prime_number_checker(i)
