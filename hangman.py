                                    #########################
                                    #     HANG MAN GAME     #
                                    #            by         #
                                    #           @AjitHX07   #
                                    #########################

import random
import hangman_design_logo
import hangman_word_list
not_end_of_game=False

#list of words
print(hangman_design_logo.logo)

game_list =hangman_word_list.game_list

stages =hangman_design_logo.stages

choosen_word = random.choice(game_list)
life =6

# print(choosen_word)
display=[]

#make the "_" in correct number of position
for _ in range(len(choosen_word)):
    display += "_"
print(display) 
#debugging

while not not_end_of_game:
    user_guess = input("Guess the word : ").lower()

    if user_guess in display:
        print(f"you already entered the letter {user_guess}")

    for position in range(len(choosen_word)):
        letter =choosen_word[position]
        # print(f"the corrent posision: {position} \n current letter: {user_guess}")
        if letter == user_guess:
            display[position] =letter     
        
    if user_guess not in choosen_word:
        print(f"sorry you guess the wrong answer {user_guess}")
        life-=1 
        if life==0:
            not_end_of_game=True
            print("my friend you loose")
       


    print(f"{' '.join(display)}")
                      
     
    print(display)    
    
    if "_" not in display:
        not_end_of_game=True
        print("YOU WIN")
    print(stages[life])