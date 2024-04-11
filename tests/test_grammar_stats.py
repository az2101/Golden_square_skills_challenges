
from lib.grammar_stats import *

"""
Given a string starting with a capital and ending with a punctuation mark
returns True
"""
def test_given_suitable_string_returns_True():
    grammar_stats = GrammarStats()
    assert grammar_stats.check('Hello world!') == True

"""
Given a string that does not start with a capital letter or end with a punctuation mark
returns False
"""
def test_given_unsuitable_string_returns_False():
    grammar_stats = GrammarStats()
    assert grammar_stats.check('Hello world') == False

"""
Given multiple strings varying between True and False outcomes
returns a percentage of 'good' strings
"""
def test_given_multpile_strings_returns_percentage():
    grammar_stats = GrammarStats()
    grammar_stats.check('Hello world!')
    grammar_stats.check('Hello world')
    grammar_stats.check('hello world')
    grammar_stats.check('This is a good string!')
    grammar_stats.check('This is not')
    grammar_stats.check('This is?')
    assert grammar_stats.percentage_good() == 50

