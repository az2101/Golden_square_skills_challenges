
from lib.reading_time import *

"""
Given a text of 200 words
It will return 1
"""
def test_reading_time_for_200_is_1():
    criteria = 1
    text = ' '.join(['word' for i in range(0, 200)])
    response = reading_time(text)
    assert criteria == response

"""
Given a text of 300 words
It will return 1
"""
def test_reading_time_for_300_is_1point5():
    criteria = 1.5
    text = ' '.join(['word' for i in range(0, 300)])
    response = reading_time(text)
    assert criteria == response

"""
Given a text of 400 words
It will return 1
"""
def test_reading_time_for_400_is_2():
    criteria = 2
    text = ' '.join(['word' for i in range(0, 400)])
    response = reading_time(text)
    assert criteria == response

"""
Given a text of 100 words
It will return 1
"""
def test_reading_time_for_100_is_point5():
    criteria = 0.5
    text = ' '.join(['word' for i in range(0, 100)])
    response = reading_time(text)
    assert criteria == response