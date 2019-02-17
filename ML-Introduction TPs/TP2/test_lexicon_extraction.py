from io import StringIO

#from lexicon_extraction import *


def test_count_sentence_long():
    # We can use a StringIO object to simulate reading from a file
    # without actually creating a temporary file for the tests
    input = StringIO("""a b c
d c a
""")
    assert count_sentences_with_word_long(input) == {'a': 2, 'c': 2, 'b': 1, 'd': 1}


def test_count_sentence():

    input = StringIO("""a b c
d c a
""")
    assert count_sentences_with_word(input) == {'a': 2, 'c': 2, 'b': 1, 'd': 1}


def test_build_cooc_long():

    src = StringIO(""" a b c a
d c a
""")
    tgt = StringIO("""A B C A
D C A
""")

    res = build_cooc_table_long(src, tgt)
    expected_res = {('c', 'C'): 2,
                    ('c', 'A'): 2,
                    ('a', 'C'): 2,
                    ('a', 'A'): 2,
                    ('c', 'B'): 1,
                    ('b', 'B'): 1,
                    ('b', 'C'): 1,
                    ('b', 'A'): 1,
                    ('a', 'B'): 1,
                    ('c', 'D'): 1,
                    ('a', 'D'): 1,
                    ('d', 'A'): 1,
                    ('d', 'D'): 1,
                    ('d', 'C'): 1}

    assert res == expected_res


def test_build_cooc():

    src = StringIO(""" a b c a
d c a
""")
    tgt = StringIO("""A B C A
D C A
""")

    res = build_cooc_table(src, tgt)
    expected_res = {('c', 'C'): 2,
                    ('c', 'A'): 2,
                    ('a', 'C'): 2,
                    ('a', 'A'): 2,
                    ('c', 'B'): 1,
                    ('b', 'B'): 1,
                    ('b', 'C'): 1,
                    ('b', 'A'): 1,
                    ('a', 'B'): 1,
                    ('c', 'D'): 1,
                    ('a', 'D'): 1,
                    ('d', 'A'): 1,
                    ('d', 'D'): 1,
                    ('d', 'C'): 1}
    
    assert res == expected_res

