from unicodedata import name
from game_data import data
from logo import logo,vs
import random
import os


def get_random_data():
    """Get data from random account"""
    return random.choice(data)

def data_account(account):
    """format account into printable format """
    name=account["name"]
    description = account["description"]
    country=account["country"]
    return f"{name}, a {description}, from {country}"


def check_answer(guess,a_followers,b_followers):
    if a_followers>b_followers:
        return guess=="a"
    else:
        return guess=="b"

def game_play():
    print(logo)
    score=0
    should_continue=True
    a_account=get_random_data()
    b_account=get_random_data()

    while should_continue:
        a_account= b_account
        b_account=get_random_data()

        while a_account==b_account:
            b_account=get_random_data()
        print(f"Compare A : {data_account(a_account)}. ")
        print(vs)
        print(f"Compare B : {data_account(b_account)}. ")

        guess=input("Who has more followers? Type 'A' or 'B' ").lower()
        a_follower=a_account["follower_count"]
        b_follower=b_account["follower_count"]
        is_correct=check_answer(guess,a_follower,b_follower)
        os.system('CLS')
        print(logo)
        if is_correct:
            score+=1
            print(f"You're right! Current score: {score}. ")
        else:
            should_continue=False
            print(f"Sorry wrong Answer. Final score: {score}")


game_play()

play_again=True
while play_again:
    user_input=input("DO you want to play again , Type 'y' to play 'n' to not ")
    if user_input =='y':
        game_play()
    else:
        play_again=False