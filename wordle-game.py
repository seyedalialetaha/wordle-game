#!/usr/bin/python3
import tkinter as tk
from tkinter import messagebox
import random

# Function to load words from 'words.txt'
def load_words():
    with open('words.txt', 'r') as file:
        words = file.read().splitlines()
    # to avoid duplicate chars in words so the logic becomes simple
    words = list(filter(lambda w: len(set(w)) == len(w), words))
    return words

# Function to select a random word
def select_word(words):
    return random.choice(words)

# Function to validate the guessed word
def validate_word(guess):
    valid_words = load_words()
    return guess in valid_words and len(guess) == 5 and guess.isalpha()

# Function to compare the guessed word with the target word
def compare_words(guess, target):
    feedback = []
    for i in range(5):
        if guess[i] == target[i]:
            feedback.append('green')  # Correct letter and position
        elif guess[i] in target:
            feedback.append('yellow')  # Correct letter but wrong position
        else:
            feedback.append('black')  # Letter not in the word
    return feedback

# Function to handle the 'Enter' button click
def on_enter():
    global attempts_left
    guess = entry.get().strip().lower()
    
    if not validate_word(guess):
        messagebox.showerror("Invalid Input", "Please enter a valid 5-letter word.")
        return
    
    feedback = compare_words(guess, target_word)
    display_feedback(guess, feedback)
    
    if guess == target_word:
        messagebox.showinfo("Well Done!", "You guessed the word correctly!")
        reset_game()
        return
    
    attempts_left -= 1
    if attempts_left == 0:
        messagebox.showinfo("Game Over!", f"The word was: {target_word}")
        reset_game()
        return
    
    entry.delete(0, tk.END)
    next_guess()

# Function to display feedback for the guessed word
def display_feedback(guess, feedback):
    for i in range(5):
        label = tk.Label(frame, text=guess[i].upper(), bg=feedback[i], fg="white", font=("Arial", 16, "bold"))
        label.grid(row=6 - attempts_left, column=i, padx=5, pady=5)

# Function to reset the game
def reset_game():
    global target_word, attempts_left
    target_word = select_word(words)
    attempts_left = 6
    entry.delete(0, tk.END)
    for widget in frame.winfo_children():
        widget.destroy()
    next_guess()

# Function to prepare for the next guess
def next_guess():
    if attempts_left > 0:
        label = tk.Label(root, text=f"Attempts left: {attempts_left}", font=("Arial", 12))
        label.grid(row=0, column=0, columnspan=5, pady=10)

# Main program
words = load_words()
target_word = select_word(words)
attempts_left = 6

# Create the main window
root = tk.Tk()
root.title("Wordle Game")

# Create a frame to hold the feedback labels
frame = tk.Frame(root)
frame.grid(row=1, column=0, columnspan=5, pady=10)

# Create an entry widget for user input
entry = tk.Entry(root, font=("Arial", 16), justify="center")
entry.grid(row=2, column=0, columnspan=5, pady=10)

# Create an 'Enter' button
enter_button = tk.Button(root, text="Enter", font=("Arial", 14), command=on_enter)
enter_button.grid(row=3, column=0, columnspan=5, pady=10)

# Create a 'Quit' button
quit_button = tk.Button(root, text="Quit", font=("Arial", 14), command=root.quit)
quit_button.grid(row=4, column=0, columnspan=5, pady=10)

# Start the game
next_guess()

# Run the main loop
root.mainloop()
