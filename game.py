# game.py
import random


print("Rock, Paper, Scissors, Shoot!")

#prompt user for input

user_choice = input("Choose 'rock' or 'paper' or 'scissors':")
print("You Chose:")
print(user_choice)

# Computer Choice

options = ["rock", "paper", "scissors"]

computer_choice = random.choice(options)
print("computer choose:") 
print(computer_choice)