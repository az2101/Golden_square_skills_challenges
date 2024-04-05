
from lib.count_words import *

"""
Given an empty string it returns 0
"""
def test_count_words_for_empty_string_is_0():
    criteria = 0
    response = count_words('')
    assert response == criteria
    
"""
Given a string of one words it returns 1
"""
def test_count_words_for_one_word_string_is_1():
    criteria = 1
    response = count_words('Hello')
    assert response == criteria

"""
Given a string of two words it returns 2
"""
def test_count_words_for_two_word_string_is_2():
    criteria = 2
    response = count_words('Hello world')
    assert response == criteria

"""
Given a string of five words it returns 5
"""
def test_count_words_for_five_word_string_is_5():
    criteria = 5
    response = count_words('Hello my name is Andrew')
    assert response == criteria