import random

play = True
wordlist_path = "/home/julian-zzl/Documents/Projects/personal/100-days-python/day-7/wordlist-hangman.txt"

logo = r'''
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                       
'''

live6 = '''
  +---+
  |   |
      |
      |
      |
      |
=========
'''

live5 = '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
'''

live4 = '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
'''

live3 = '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
'''

live2 = '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
'''

live1 = r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
'''

live0 = r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
'''

def print_hangman(lives):
    match lives:
        case 0:
            print(live0)
        case 1:
            print(live1)
        case 2:
            print(live2)
        case 3:
            print(live3)
        case 4:
            print(live4)
        case 5:
            print(live5)
        case 6:
            print(live6)


def choise_play_again(lives):
    message = "Do you want to play again? y/n: "
    if lives == 0:
        continue_playing = input("You lost! Do you want to play again? y/n: ").strip().lower()
    else:
        print("You guessed the word. You win!")
        continue_playing = input(message).strip().lower()
    while continue_playing not in ('y', 'n'):
        print("Incorrect choice, write either 'y' or 'n'")
        continue_playing = input(message).strip().lower()
    if continue_playing == 'y':
        return True
    else:
        return False

line_count = 0
file_content = ""

with open(wordlist_path, 'r') as file:
    contents = file.read()
    line_count = int(contents.count('\n'))
    contents = contents.split("\n")
    file.close()

while play:
    lower_cases = ""
    letter_indexes = []
    total_lives = 6
    guessed_letters = []
    lives = total_lives
    alive = True
    random_word = random.randint(0 , line_count)
    word = contents[random_word]
    word_len = len(word)

    for i in range(word_len):
        lower_cases += '_'

    print(logo)
    print(word)

    print(f"Word to guess: {lower_cases}")

    guess_letter = input("Guess a letter: ")
    guessed_letters.append(guess_letter)
    if guess_letter not in word:
        lives -= 1
        print(f"You guessed {guess_letter} that's not in the word. You lose a life")
        print(live5)
    else:
        index = 0
        index = word.index(guess_letter, index)
        letter_indexes.append(index)
        while index != -1:
            try:
                index = word.index(guess_letter, index + 1)
                letter_indexes.append(index)
            except:
                break

        # Reeplaces the guessed character according to the indexes in the word
        for i in range(len(letter_indexes)):
            lower_cases = list(lower_cases)
            lower_cases[letter_indexes[i]] = guess_letter
        letter_indexes = []
        lower_cases = ''.join(lower_cases)
        print(lower_cases)
        print(live6) 

        #reset indexes for next letter to guess
    # Play loop after discovering or failing the first letter
    while lives != 0:
            print(f"****************************{lives}/{total_lives} LIVES LEFT****************************")
            print(f"Word to guess: {lower_cases}")
            guess_letter = input("Guess a letter: ")
            if guess_letter in guessed_letters:
                print(f"You already guessed '{guess_letter}'")
                continue
            if guess_letter not in word:
                lives -= 1
                print(f"You guessed '{guess_letter}' that's not in the word. You lose a life")                
                print_hangman(lives)
                if lives == 0:
                    play = choise_play_again(lives)
                continue
            else:
                index = 0
                index = word.index(guess_letter, index)
                letter_indexes.append(index)
                while index != -1:
                    try:
                        index = word.index(guess_letter, index + 1)
                        letter_indexes.append(index)
                    except:
                        break

                # Reeplaces the guessed character according to the indexes in the word
                for i in range(len(letter_indexes)):
                    lower_cases = list(lower_cases)
                    lower_cases[letter_indexes[i]] = guess_letter
                lower_cases = ''.join(lower_cases)
                print(lower_cases)
            letter_indexes = []

            print_hangman(lives)


            if lower_cases == word:
                play = choise_play_again(lives)
                lives = 0
                

    lives = 0
    lower_cases = ''
    word = ''
    continue_playing = ''