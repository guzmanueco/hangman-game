from encoding_functions import cleaning_accents, cleaning_uppercase
import string
import unicodedata
from sentences import all_sentences
import random

lower = list(string.ascii_lowercase)
upper = list(string.ascii_uppercase)
letters = lower + upper

example = random.choice(all_sentences)

cleant_sentence=cleaning_uppercase(cleaning_accents(example))


def initial_state(sentence):
    output = ''
    for e in sentence:
        if e in letters:
            output += '-'
        else:
            output += e
    return output


game_status = list(initial_state(example))

said_letters = []

failures = 0

def finding_index(letter, sentence):
    return [i for i,e in enumerate(cleant_sentence) if cleant_sentence[i]==letter]

def guessing_letter(letter, sentence):
    global failures
    indexes = finding_index(letter, sentence)
    said_letters.append(letter)
    while failures < 10:
        if indexes:
            for i in indexes:
                game_status[i] = sentence[i]
            output = ''.join(game_status)
            if not output == sentence:
                return output + '\nLetters said: {}\n'.format(' '.join(said_letters))
            else:
                print(output + "\nCongratulations, you won")
                exit()
        else:
            failures +=1
            print(''.join(game_status))
            return '\nFail! You have {} lifes left.\nLetters said: {}\n'.format(10-failures,' '.join(said_letters))
    print('Game over\nSentence was: {}'.format(sentence))
    exit()

def full_game():
    print(initial_state(example)+'\n')
    while failures <= 10:
        a = input('Enter your letter: ')
        print(guessing_letter(a, example))
