from pickle import FALSE
from tkinter import Y
from logo import logo,logo1,logo2,logo3,logo4,logo5
import os
import random

EASY_LEVEL_TURN=10
HARD_LEVEL_TURN=5
def random_no_genrator():
    return random.randint(1,100)

def ans_check(user_ans,random_no,turn):
    if user_ans>random_no:
        print("TOO HIGH")
        return turn-1
    elif user_ans<random_no:
        print("TOO LOW")
        return turn-1
    elif user_ans==random_no:
        print(logo4)
        print(" ~'.* YOU GOT THE ANSWER *.'~ ")
    
def set_dificulty():
    os.system('CLS')
    print(logo1)
    user_ans1=input("Type your ans here :").lower()
    if user_ans1=='easy':
        os.system('CLS')
        print(logo2)
        return EASY_LEVEL_TURN
    elif user_ans1=='hard':
        os.system('CLS')
        print(logo2)
        return HARD_LEVEL_TURN
    else:
        print("(╯°□°)╯︵ ɹoɹɹƎ ")

def play_game():
    print (logo)
    user_ans=input("Type 'y' to play the game 'n' not to.")
    if user_ans=='y':
        answer=random_no_genrator()
        turns=set_dificulty()
        guess=0
        while guess!=answer:
            print(f"You have {turns} attempts remaining to guess a number.")
            guess=int(input("Make a guess : "))
            turns=ans_check(guess,answer,turns)
            if turns==0:
                print(logo5)
                print("You've run out of guesses, you lose.")
                print(f"MY number was {answer}")
                return
            elif guess!=answer:
                print("Guess again")

    else:
        os.system('CLS')
        print(logo3)

should_continue=False
while not should_continue:
    play_game()
    user_input=input("Do you want to play again type 'y' else 'n'")
    if user_input=='y':
        os.system('CLS')
    else:
        should_continue=True