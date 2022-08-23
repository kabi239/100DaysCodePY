# Hungman
import random
from D7_wordlist import word_list
from ASCCI_ART import stages,logo


def Rules():
    print("Hangman is a simple word guessing game. Players try to figure out an unknown word by guessing letters. If too many letters which do not appear in the word are guessed, the player is hanged (and loses). \n \n As letters in the word are guessed, write them above the cooresponding underline. If a letter not in the word of guess, draw a picture of a person on the gallow–one part for each incorrect letter guess. Most frequently, the person is drawn in 6 parts (for 6 letter guesses) in the order: head, body, left leg, right leg, left arm, right arm.\n" )
def game():
    lives=6
    end_of_game=False
    chosen_word=random.choice(word_list)
    #print(chosen_word)

    word_display=[]
    for i in chosen_word:
        word_display.append("_")
    print(word_display)

    while not end_of_game:
        guess=input("guess a word : \n").lower()
        if guess in word_display:
          print(f"You,ve already guessed the letter {guess}\n")
        for i in range(0,len(chosen_word)):
            if chosen_word[i]==guess:
                word_display[i]=guess
            
        print(word_display)
        print("\n")
        if guess not in chosen_word:
          print(f"You guessed {guess}, that's not in the word. You lose a life.\n")
          lives-=1
          print(stages[lives])
          if lives==0:
              end_of_game=True
              print(stages[0])
              print("\nYou Lose.\n")
              print(f"Word is : {chosen_word}\n")

        print(lives)
        if "_" not in word_display:
            end_of_game= True
            print("\nYou Win!\n")


print(logo)
print(stages[0])

user_input=input("Write Y/y to know the rules or N/n to directly start the game\n").lower()

if user_input=='y':
    Rules()
    game()
elif user_input=='n':
  game()
else:
  print("WRONG INPUT")