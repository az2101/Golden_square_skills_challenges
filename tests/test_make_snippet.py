
from lib.make_snippet import *

""" Given a string of words, returns the string"""

'''def test_given_string_returns_string():
    result = make_snippet('Hello my name is Andrew and this is my string')
    
    assert result == 'Hello my name is Andrew and this is my string'
'''
"""Given a string of words, needs to split the string into a list of words"""

'''def test_splits_string_into_list_of_words():
    result = make_snippet('Hello my name is Andrew and this is my string')

    assert result == ['Hello', 'my', 'name', 'is', 'Andrew', 'and', 'this', 'is', 'my', 'string']'''

''' Given a string of words returns a the first 5 words as a list'''

'''def test_splits_string_and_gives_first_5_words_as_list():
    result = make_snippet('Hello my name is Andrew and this is my string')

    assert result == ['Hello', 'my', 'name', 'is', 'Andrew']'''

'''given a string of words, returns first 5 words as a string'''

def test_make_snippet_functions():
    result = make_snippet('Hello my name is Andrew and this is my string')
    assert result == 'Hello my name is Andrew...'

