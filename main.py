import random
from art import logo
life = 0
choosen_number = []
game_is = True

def select_number():
    """ function to choose the number"""
    number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 , 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55,56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]
    guess_number = random.choice(number_list)
    choosen_number.append(guess_number)
    return choosen_number

print(logo)
print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
level = input("Choose a difficulty. Type 'easy' or 'hard: " ).lower()
if level == ("easy"):
    life += 10
elif level == ("hard"):
    life += 5
else:
    print("you type a invalid caracter")

select_number()
#print (f"Select number = {choosen_number [0]}")

#game
while game_is == True and life > 0:
    print(f"you have {life} attempts to guess the number")
    player_guess = int(input("make a guess: "))
    if player_guess == choosen_number [0]:
        print (f"You reach the number! it was {choosen_number [0]}")
        game_is = False
    elif life > 0:
        if player_guess > choosen_number [0]:
            print ("too high")
            life -= 1
        elif player_guess < choosen_number [0]:
            print ("too low")
            life -= 1
if life == 0:
    print(f"Game over, the number was {choosen_number [0]}")
    game_is = False

