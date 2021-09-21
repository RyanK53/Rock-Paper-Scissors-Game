# game.py
import random


print("Rock, Paper, Scissors, Shoot!")

#prompt user for input

user_choice = input("Choose 'Rock' or 'Paper' or 'Scissors':")
print("You Chose:")
print(user_choice)

# Computer Choice

options = ['Rock', 'Paper', 'Scissors']

computer_choice = random.choice(options)
print("Computer Chose:") 
print(computer_choice)

breakpoint()

if (user_choice != 'Rock' or 'Paper' or 'Scissors'):
    print("Hey! that isn't right, try it again, remember, capitalization matters!")
elif(user_choice == computer_choice):
    print("Draw, try again!")
elif(user_choice == 'Rock' and computer_choice == 'Scissors'):
    print("You win! Nice Job")
elif(user_choice == 'Paper' and computer_choice == 'Scissors'):
    print("You lose :( try again next time!")
elif(user_choice == 'Scissors' and computer_choice == 'Rock'):
    print("You lose :( try again next time!")
elif(user_choice == 'Scissors' and computer_choice == 'Paper'):
    print("You win! Nice Job")
elif(user_choice == 'Rock' and computer_choice == 'Paper'):
    print("You lose :( try again next time!")
elif(user_choice == 'Paper' and computer_choice == 'Rock'):
    print("You win! Nice Job")