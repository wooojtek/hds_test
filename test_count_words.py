# run this test by using py.test:
# (pip install pytest)
# $> py.test -k test_count_words

from count_words import count_words


def test_count_words():
    textfile, n = 'words.md', 5

    expected_top_five = ['the', 'a', 'of', 'and', 'file']
    assert count_words(textfile, n)[:5] == expected_top_five
