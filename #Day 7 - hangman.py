#Day 7 - hangman
import art
from hangman_words import word_list
import os
import random

# Clear screen after every run
os.system("cls")

# import the logo of the game
print(art.logo)

# Variables
chances = len(art.stages) - 1
game_over = False
spaces = []
correct_guess= 0

# Getting random words to guess
word = random.choice(word_list)
word = 'razzmatazz'
# TESTING PURPOSE. REMOVE IN FINAL ADDITION
print(f"For testing only: the word is {word}")

# Inputs
guess = input(f"Guess a letter: ")


for char in word:
    spaces.append("_ ")
    
# while chances > 0:
if guess in word:
    for char in range(len(word)):
        if word[char] == guess:
            spaces[char] = guess
    print("".join(spaces))
    correct_guess += 1
else:
    print(f"You guessed {guess}, that's not in the word. You lose a life.") 
    print("".join(spaces))
    print(art.stages[chances])
    chances -= 1
    


