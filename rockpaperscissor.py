import tkinter as tk
from tkinter import messagebox
import random

def play_game(user_choice):
    computer_choices = [0, 1, 2]
    meanings = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(computer_choices)

    user_text = meanings[user_choice].upper()
    computer_text = meanings[computer_choice].upper()

    result = ""
    if user_choice == computer_choice:
        result = "It's a draw!"
    elif (user_choice - computer_choice) % 3 == 1:
        result = "You win!"
    else:
        result = "Computer wins!"

    messagebox.showinfo("Result", f"YOU: {user_text}\nCOMPUTER: {computer_text}\n\n{result}")

def main():
    root = tk.Tk()
    root.title("Rock-Paper-Scissors Game")

    label = tk.Label(root, text="Choose your move:")
    label.pack()

    button_rock = tk.Button(root, text="Rock", command=lambda: play_game(0))
    button_rock.pack()

    button_paper = tk.Button(root, text="Paper", command=lambda: play_game(1))
    button_paper.pack()

    button_scissors = tk.Button(root, text="Scissors", command=lambda: play_game(2))
    button_scissors.pack()

    root.mainloop()

if __name__ == "__main__":
    main()
