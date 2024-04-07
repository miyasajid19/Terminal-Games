import random
import sys
count=5
computer=random.randint(1,100)
print('i have the number stored in my memory\nnow i want you to guess the number in 5 attempt\nthe hint i want to give to you is this is from 1 to 99')
while True:
    user=int(input(f'Now guess the number and you have {count} guess left'))
    
    if user>=100 or user<1:
        print("this is invalid input")
    elif user==computer:
        print("Congratulation!! You have guessed the right answer")
        sys.exit()
    elif user>computer:
        count=count-1
        print("your guess is high")
    elif user<computer:
        count=count-1
        print("your guess is low")

    if count==0:
        print(f"OOPS!! you have no more guess left\ni have stored {computer}\nsorry!!\nTRY AGAIN")
        sys.exit()