import random
list=['rock', 'paper', 'scissors']
while True:
    user = input("Enter Rock, Paper, or Scissors: ").lower()
    if user in list:
        break  # Break the loop if the input is valid
    else:
        print("Invalid input! Please enter either 'rock', 'paper', or 'scissors'.")

user=random.choice(list)
computer=random.choice(list)
if computer==user:
    format=f"computer chooses {computer}\nuser chooses {user}\nits draw!!\n\n"
    print(format)
elif computer=='rock' and user=='paper':
    format=f"computer chooses {computer}\nuser chooses {user}\nuser wins!!\n\n"
    print(format)
elif user=='rock' and computer=='paper':
    format=f"computer chooses {computer}\nuser chooses {user}\ncomputer wins!!\n\n"
    print(format)
elif computer=='paper' and user=='scissors':
    format=f"computer chooses {computer}\nuser chooses {user}\nuser wins!!\n\n"
    print(format)
elif computer=='scissors' and user=='paper':
    format=f"computer chooses {computer}\nuser chooses {user}\ncomputer wins!!\n\n"
    print(format)
elif computer=='scissors' and user=='rock':
    format=f"computer chooses {computer}\nuser chooses {user}\nuser wins!!\n\n"
    print(format)
else:
    format=f"computer chooses {computer}\nuser chooses {user}\ncomputer wins!!\n\n"
    print(format)

f=open("rockpaperscissor.txt",'a')
f.write(format)
f.close()