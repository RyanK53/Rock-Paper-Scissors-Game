# game.py
import random
user_name = input("Hello, what is your name: ")
print("----------------")
print("Welcome, let's play Rock, Paper, Scissors")
print("----------------")
#prompt user for input
user_choice = input("Choose 'Rock' or 'Paper' or 'Scissors':")
print("-----------------")
print("You Chose:")
print(user_choice) 
print("-----------------")



# Computer Choice

options = ['Rock', 'Paper', 'Scissors']

computer_choice = random.choice(options)
print("Computer Chose:") 
print(computer_choice)
print("-----------------")


if(user_choice == computer_choice):
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
elif(user_choice != 'Rock' or 'Paper' or 'Scissors'):
    print("That doesn't look right, try again, remember, capitalization matters")

print("-----------------")
print("Thank you for playing")
print(user_name) 

