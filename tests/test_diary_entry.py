import pytest
from lib.diary_entry import *

"""
Given an empty title and contents
Raises an error
"""
def test_errors_on_empty_title_and_contents():
    with pytest.raises(Exception) as err:
        DiaryEntry("","")
    assert str(err.value) == "Diary entries must have a title or contents"


""" 
Given a title and contents
format returns a formatted entry like
'my title: these are the contests'
"""

def test_formats_with_title_and_contents():
    diary_entry = DiaryEntry("My Title", "my contents")
    result = diary_entry.format()
    assert result == "My Title: my contents"

"""
Given a title and contents
counts the number of words in the entry
"""
def test_count_words_counts_words_in_entry():
    diary_entry = DiaryEntry('My Title', 'my contents')
    result = diary_entry.count_words()
    assert result == 4

"""
Given a wpm of 2
and a text of 2 words
returns 1 minute
"""

def test_reading_time_with_fourwpm_and_fourwords():
    diary_entry = DiaryEntry('My Title', 'one two')
    result = diary_entry.reading_time(2)
    assert result == 1

"""
Given a wpm of 2
and text with 4 words
returns 2 minutes
"""
def test_reading_time_with_twowpm_and_fourwords():
    diary_entry = DiaryEntry('My Title', 'one two three four')
    result = diary_entry.reading_time(2)
    assert result == 2

"""
Given a wpm and number of minutes
return a chunk of contents that can be read in this time
"""

def test_wpm_of_two_and_two_minutes_returns_four_words_of_contents():
    diary_entry = DiaryEntry('My Title', 'one two three four five six seven eight')
    assert diary_entry.reading_chunk(2, 2) == 'one two three four'

"""
Given a content of 8 words
and a wpm 2 and 2 mins
first time returns 'one two three four'
second time returns 'five six seven eight'
"""   

def test_reading_chunk_called_multiple():
    diary_entry = DiaryEntry('My Title', 'one two three four five six seven eight')
    assert diary_entry.reading_chunk(2, 2) == 'one two three four'
    assert diary_entry.reading_chunk(2, 2) == 'five six seven eight'
    assert diary_entry.reading_chunk(2, 2) == 'one two three four'

