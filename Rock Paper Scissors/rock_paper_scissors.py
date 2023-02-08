import tkinter as tk
from tkinter import messagebox
import random

def play_game():
    user_choice = user_var.get()
    computer_choice = random.choice(['rock', 'paper', 'scissors'])

    if user_choice == computer_choice:
        result_text.set("Tie!")
    elif (user_choice == "rock" and computer_choice == "scissors") or (user_choice == "paper" and computer_choice == "rock") or (user_choice == "scissors" and computer_choice == "paper"):
        result_text.set("You win!")
    else:
        result_text.set("You lose!")
        
    # Reset the user's choice
    user_var.set(None)

def play_again():
    result_text.set("")
    computer_choice_label.config(text="")
    root.deiconify()
    start_window.destroy()

def quit_game():
    root.destroy()
    start_window.destroy()

def start_screen():
    global start_window
    start_window = tk.Tk()
    start_window.title("Welcome to Rock-Paper-Scissors")

    welcome_label = tk.Label(start_window, text="Welcome to Rock-Paper-Scissors!" ,font=("Helvetica", 16))
    instruction_label = tk.Label(start_window, text="Please select your choice and click Play to start the game.", font=("Helvetica", 14))
    start_button = tk.Button(start_window, text="Start", command=root.deiconify, font=("Helvetica", 14))

    welcome_label.pack(padx=20, pady=20)
    instruction_label.pack(padx=20, pady=20)
    start_button.pack(padx=20, pady=20)

    start_window.mainloop()

root = tk.Tk()
root.title("Rock-Paper-Scissors")
root.withdraw()

# Create variables to hold user's choice and result text
user_var = tk.StringVar()
result_text = tk.StringVar()

# Create radio buttons for user to select their choice
rock_button = tk.Radiobutton(root, text="Rock", variable=user_var, height=5,width=10 , value="rock", font=("Helvetica", 16))
paper_button = tk.Radiobutton(root, text="Paper", variable=user_var,height=5,width=10 ,value="paper", font=("Helvetica", 16))
scissors_button = tk.Radiobutton(root, text="Scissors", variable=user_var, height=5,width=10 , value="scissors", font=("Helvetica", 16))

# Create a label to display the result of the game
result_label = tk.Label(root, textvariable=result_text, font=("Helvetica", 16))
computer_choice_label = tk.Label(root, text="", font=("Helvetica", 16))

# Create buttons for the user to play again or quit the game
play_again_button = tk.Button(root, text="Play Again", command=play_again, font=("Helvetica", 14),height=5,width=10)
quit_button = tk.Button(root, text="Quit", command=quit_game, font=("Helvetica", 14),height=5,width=10)

play_button = tk.Button(root, text="Play", command=play_game, font=("Helvetica", 14),height=5,width=10)

rock_button.pack(pady=20)
paper_button.pack(pady=20)
scissors_button.pack(pady=20)
play_button.pack(pady=20)
result_label.pack()
computer_choice_label.pack()
play_again_button.pack(padx=20, pady=20)
quit_button.pack()

start_screen()
root.mainloop()