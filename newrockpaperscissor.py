import random
list1=['rock', 'paper', 'scissors']
while True:
    user = input("Enter Rock, Paper, or Scissors: ").lower()
    if user in list1:
        from  functionforallgame import rps
        rps(list1)
        break
    else:
        print("Invalid input! Please enter either 'rock', 'paper', or 'scissors'.")


