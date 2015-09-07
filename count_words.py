from collections import Counter
from operator import itemgetter
import re


def count_words(textfile, n):
    """
    file int -> list of str
    :param textfile: text file e.g. words.md
    :param n: natural number
    :return: list of words in order of occurance and alphabetical

    Time taken to complete the task: approx. an hour
    Sources: https://github.com/CrowdScores/py-wojciech/tree/master/001-counting-words

    """

    file = open(textfile, 'r+')
    chars = file.read()
    file.close()
    # remove non-alphanumeric characters, convert to lowercase and split
    words = re.sub(r'[^a-zA-Z0-9]', ' ', chars).lower().split()
    # ordered list of word-occurance pairs in range n
    words = Counter(words).most_common()
    # sort words alphabetically
    words = sorted(words)
    # sort words by occurrence number
    words = sorted(words, key=itemgetter(1), reverse=True)
    # produce word only
    return [word[0] for word in words][:n]
