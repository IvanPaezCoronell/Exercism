import string
from collections import defaultdict


def count_words(sentence):
    count = defaultdict(int)
    sentence = ' '.join(sentence.split(','))
    sentence = ' '.join(sentence.split('_'))
    for password in string.punctuation.replace("'", ""):
        sentence = sentence.replace(password, "")
    for letter in sentence.split():
        letter = letter.strip("'")
        count[letter.lower()] += 1
    return count
