from unidecode import unidecode
import string

def cleaning_accents(str):
    return unidecode(str)

def cleaning_uppercase(str):
    return str.casefold()

