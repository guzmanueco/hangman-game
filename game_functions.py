from encoding_functions import cleaning_accents, cleaning_uppercase
import string
import unicodedata

lower = list(string.ascii_lowercase)
upper = list(string.ascii_uppercase)
letters = lower + upper

example = 'Hello world!'


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
    indexes = finding_index(letter, sentence)
    said_letters.append(letter)
    fails = failures
    
    if indexes:
        for i in indexes:
            game_status[i] = sentence[i]
        output = ''.join(game_status)
        if not output == sentence:
            return output + '\nLetters said: {}'.format(' '.join(said_letters))
        else:
            return output + "\nCongratulations, you won"
    else:
        fails +=1
        if fails > 10:
            return 'Game over\nSentence was: {}'.format(sentence)
        return 'Fail! You have {} lifes left.\nLetters said: {}'.format(10-fails,' '.join(said_letters))




print(guessing_letter('h',example))
print(guessing_letter('e', example))
print(guessing_letter('l', example))
print(guessing_letter('o', example))
print(guessing_letter('w', example))
print(guessing_letter('r', example))
print(guessing_letter('d', example))

