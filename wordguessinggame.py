from functionforallgame import wordguessinggame
print("this is word guessing game")
print("i have a word now its you turn to guess the word")
print("i will give you first 4 letters as hint")
while True:
    choice=input("are you Familiar with the rules? press Yes or No").lower()
    if choice=="yes":
        wordguessinggame()
        break
    else:
        print("rule no 1: computer stores the word and gives you hints of random index and display other characters blank")
        print("you have to guess the word")
        print("then you will be asked input")
        print("if your given word is correct you won the game")
        print("else only first letter of your given word is chosen as the valid input charcter")
        print("you have unlimited choices to made")
        print("this program will run till you guessed the word correctly")
        x=input("do you understand? yes or no").lower()
        print('\n\n\n\n\n\n')
        if x=="yes":
            wordguessinggame()
        