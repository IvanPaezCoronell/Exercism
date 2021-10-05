import string


def is_pangram(sentence):
    sen = set(sentence.lower()).issuperset(set(string.ascii_lowercase))
    return sen
