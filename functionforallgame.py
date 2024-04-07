def hangman_game(player1,hints):
    life = 7
    original = list(player1)
    player2 = ['-'] * len(player1)

    while life != 0:
        status(life)
        print("hints is : ",hints)
        print(f"You have {life-1} lives left")
        take = input("Guess the letter: ").lower()
        
        take = take[0]

        if take not in original:
            life -= 1
        else:
            for i, letter in enumerate(original):
                if letter == take:
                    player2[i] = take  
        print(player2)
        if life==1:
            print(f"You lose!! Try again\n the word was {player1}")
            break
        if "".join(player2) == player1:
            print('Congratulations! You won!')
            break


def status(life):
    if life == 7:
        print("           ----------")
        print('          |         |')
        print('                    |')
        print('                    |')
        print('                    |')
        print('                    |')
        print('                    |')
        print('       =======================')
    elif life == 6:
        print("           ----------")
        print('          |         |')
        print('          0         |')
        print('                    |')
        print('                    |')
        print('                    |')
        print('                    |')
        print('       =======================')
    elif life == 5:
        print("           ----------")
        print('          |         |')
        print('          0         |')
        print('          |         |')
        print('          |         |')
        print('                    |')
        print('                    |')
        print('       =======================')
    elif life == 4:
        print("           ----------")
        print('          |         |')
        print('          0         |')
        print('          |         |')
        print('         /|         |')
        print('          |         |')
        print('                    |')
        print('       =======================')
    elif life == 3:
        print("           ----------")
        print('          |         |')
        print('          0         |')
        print('          |         |')
        print('         /|\\       |')
        print('          |         |')
        print('                    |')
        print('       =======================')
    elif life == 2:
        print("           ----------")
        print('          |         |')
        print('          0         |')
        print('          |         |')
        print('         /|\\        |')
        print('          |         |')
        print('         /          |')
        print('       =======================')
    elif life == 1:
        print("           ----------")
        print('          |         |')
        print('          0         |')
        print('          |         |')
        print('         /|\\        |')
        print('          |         |')
        print('         / \\        |')
        print('       =======================')
        print("you have no life left.\nHence,")
        print('Game over! The word was:', "".join(original))
        
def bot():
    import random
    import time

    user = []
    computer = []
    chance = ['user', 'computer']
    turn = random.choice(chance)

    for x in range(6):
        if turn == 'user':
            c = random.randint(1, 11)
            user.append(c)
            time.sleep(3)
            print("User got : ",user)
            turn = 'computer'
        else:
            c = random.randint(1, 11)
            computer.append(c)
            time.sleep(3)
            print("Computer got :",computer)
            turn = 'user'

    print('result is being calculated')
    time.sleep(5)
    if sum(user)>21 and sum(computer)<21:
        print("user total sum is greater than 21 and computer sum is less than 21 'so computer wins")
    elif sum(user)==21 and sum(computer)==21:
        print("its Draw")
    elif sum(computer)>21 and sum(user)<21:
        print("computer total sum is greater than 21 and user sum is less than 21 'so user wins")
    elif sum(user)==21:
        print('CONGRATULATIONS you  won')
    elif sum(computer)==21:
        print('computer won') 
    elif sum(user)>sum(computer):
        print('CONGRATULATIONS you  won')
    else:
        print('computer')
    
    
    
def rps(list1):
    import random
    user=random.choice(list1)
    computer=random.choice(list1)
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
    

def wordguessinggame():
    import random
    import sys
    words = [
    'programming', 'cybersecurity', 'intelligence', 'javascript', 'application', 'development',
    'encryption', 'blockchain', 'framework', 'integration', 'cloud', 'javascript', 'python', 'database',
    'scalability', 'debugging', 'networking', 'functionality', 'programming', 'automation', 'algorithm',
    'customization', 'virtualization', 'accessibility', 'optimization', 'information', 'performance',
    'authentication', 'authorization', 'interoperability', 'configuration', 'personalization', 'flexibility',
    'infrastructure', 'productivity', 'technological', 'sustainability', 'collaboration', 'integration',
    'intelligence', 'architecture', 'documentation', 'datacenter', 'improvement', 'vulnerability',
    'implementation', 'augmented', 'responsive', 'customization', 'maintenance', 'compatibility', 'javascript',
    'programming', 'development', 'cybersecurity', 'engineering', 'optimization', 'authentication',
    'authorization', 'interoperability', 'configuration', 'personalization', 'flexibility', 'infrastructure',
    'productivity', 'technological', 'sustainability', 'collaboration', 'integration', 'intelligence',
    'architecture', 'documentation', 'datacenter', 'improvement', 'vulnerability', 'implementation',
    'augmented', 'responsive', 'customization', 'maintenance', 'compatibility', 'javascript', 'programming',
    'development', 'cybersecurity', 'engineering'
]


    chosenword=random.choice(words)
    chosenwordlist=list(chosenword)
    lengthofchosenword=len(chosenword)
    guessedword=["-"]*lengthofchosenword
    indexforchosenword=[x for x in range(lengthofchosenword)]
    duplicateofindex=indexforchosenword
    hints=list()
    for x in range(4):
        y=random.choice(duplicateofindex)
        try:
            duplicateofindex.remove(y)
        except Exception as e:
            print(e)
        hints.append(y)
   
    for index,value in enumerate(chosenword):
        if index in hints:
            print(value,end='')
        else:
            print("-",end="")
    while True:
        guessedword=''
        status=True
        while status==True:
            user=input("guess the word :").lower()
            if user!=None:
                print("Null input is not accepted")
                status=False
                
        if user==chosenword:
            print(f"yes! {user} is the correct word.")
            sys.exit()
        else:
            print("the entered word doesn't matched the word so firs")
            user=list(user)
            try:
                user=user[0]
            except Exception as p:
                print(p)
            for index,value in enumerate(chosenword):
                if index in hints:
                    print(value,end='')
                    guessedword=guessedword+value
                else:
                    if user==chosenword[index]:
                        print(value,end='')
                        hints.append(index)
                        guessedword=guessedword+value
                    else:
                        print("-",end="")
                        guessedword=guessedword+'-'
        if guessedword==chosenword:
            print(f"yes! {guessedword} is the correct word.")
            sys.exit()
        
                    