import random                   #random function for random selection
from words import words            #import words from list 


# put game in a function. Call at the end and allows restart.
def game():

    # options for easy, medium and hard with different amount of turns
    print(f'Welcome to Hangman!')
    print(f'1 for Easy level = 8 turns')
    print(f'2 for Medium level = 6 turns')
    print(f'3 for Hard level = 4 turns')

    word = random.choice(words)                 #randomly selects word from our list. Add more words over time.
    letters_guessed = ''                        #keep count of letters guessed
    playing = True                              #will use to restart game at end

   
    difficulty = input('Please select difficulty level: ')
    if difficulty == '1':
        max_turns = 8
    elif difficulty == '2':
     max_turns = 6
    elif difficulty =='3':
        max_turns = 4
    else:
        print(f'Please select a number between 1-3.')

    # loop for max turns. Will break loop if player succeeds     
    
    while max_turns > 0:
    #receive guess from player
        guess = input(' Enter a letter: ').lower()
        if guess in word:
            print(f'You guessed correctly. There is one or more {guess} in the secret word.')
        else:
            max_turns -=1
            print('Sorry. That letter is not in the secret word.')

    # account for list of guesses
        letters_guessed = letters_guessed + guess
        wrong_letter_count = 0

        for letter in word:
            if letter in letters_guessed:
                print(f'{letter}', end = ' ')
            else:
                print('_', end= ' ')
                wrong_letter_count += 1

        if wrong_letter_count == 0:
            print(' Congratulations! You win!') 
            break                                   #break applies to while loop at line 31
    else:
        print(f'Sorry. You lose :( ') 

    restart = input("Play again? (y/n): ").lower()
    if not restart == 'y':
        playing = False
    else:
        game()

            
game()












