from functionforallgame import hangman_game
player1=input("Enter the word that you want to ask to player 2 ").lower()
print(" give hints to the player 2: ")
hints=input()
hangman_game(player1,hints)