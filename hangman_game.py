import random

def add_word():
    new_word = input('Which word you want to add: ').lower()
    with open('./hangman_words.txt', 'r') as r:
        words_file= r.read()
        assert new_word not in words_file, (f'The word {new_word} is in the file.')
        assert new_word.isnumeric() == False, (f'{new_word} is a number not a word.')
        with open('./hangman_words.txt', 'a') as a:
            a.write(new_word)
            a.write('\n')
        
        a.close()
    r.close()

def remove_word():
    remove_word = input('Which word you want to remove: ').lower()
    with open('./hangman_words.txt', 'r') as r:
        words_file= [i.rstrip() for i in r.readlines()]
        word_removed = list(filter(lambda x: x != remove_word, words_file))
        with open('./hangman_words.txt', 'w') as w:
            for word in word_removed:
                w.write(word)
                w.write('\n')
        w.close()
    r.close()

def word():
    with open('./hangman_words.txt', 'r') as r:
        choose_word = [word.rstrip() for word in random.choices(r.readlines())]
    r.close()

    choosen_word = ''
    for i in choose_word:
        choosen_word += i

    choosen_word =  [word for word in choosen_word]
        
    return choosen_word


def play():
    play_word = word()    
    
    given_letter = []
    guess_word = []
    for i in play_word:
        guess_word.append('_')

    while '_' in guess_word:
        print(f"Letter you've given {given_letter}")
        print(f"Guessing word {guess_word}")

        try:
            print('\n')
            letter = input('Try a letter: '.lower())
            if letter.isnumeric() == True:
                raise Exception(f'{letter} is not a letter, try to type a letter')
        except Exception as e:
            print(e)
                       
        
        if letter in play_word:
            for index, i in enumerate(play_word):
                if play_word[index] == letter:
                    guess_word[index] = letter
        
        elif letter not in play_word:
            given_letter.append(letter)


        if '_' not in guess_word:
            winning_word = ''.join(play_word)
            print(f'You won, the word was {winning_word.upper()}')



def run(option):
    if option == 'a':
        play()
    elif option == 'b':
        add_word()
    elif option == 'c':
        remove_word()
    else:
        print("that's not an option")

if __name__ == '__main__':
    print('W E L C O M E  T O  T H E  H A N G M A N  G A M E')
    option = input(
    """TYPE AND OPTION
    A. PLAY
    B. ADD A WORD
    C. DELETE A WORD

    """).lower()
    print('\n')

    run(option)