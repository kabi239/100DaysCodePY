# Rock Paper Scissors
import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]
user_input=int(input("What do you choose? Type 0 for Rock, 1 for paper or 2 for Scissors : "))
if user_input>=3 or user_input <00:
    print("You typed an invalid number, you lose!")
else:
    print(game_images[user_input])
    computer_choice=random.randint(0,2)
    print("Computer chose: ")
    print(game_images[computer_choice])
    if user_input == 0 and computer_choice == 2:
        print("✌⊂(✰ ‿ ✰) つ✌ xxx You win! xxx ✌⊂(✰ ‿ ✰ ) つ✌")
    elif computer_choice == 0 and user_input == 2:
        print("(✖ ╭╮ ✖ ) --- You lose --- (✖ ╭╮ ✖ )")
    elif computer_choice > user_input:
        print("(✖ ╭╮ ✖ ) --- You lose --- (✖ ╭╮ ✖ )")
    elif user_input > computer_choice:
        print("✌⊂(✰ ‿ ✰ ) つ✌ xxx You win! xxx ✌⊂( ✰ ‿ ✰ ) つ✌")
    elif computer_choice == user_input:
        print("ˁ(⦿ ᴥ ⦿ )ˀ It's a draw ˁ(⦿ ᴥ ⦿ )ˀ")

