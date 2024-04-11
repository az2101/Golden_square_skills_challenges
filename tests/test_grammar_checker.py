
from lib.grammar_checker import *

"""
Given a string starts with a capital letter and ends with a punctuation mark
Returns True
"""
def test_grammar_checker_for_capital_and_punct_returns_true():
    criteria = True
    response = grammar_checker('Hello World!')
    assert criteria == response


"""
Given a string starts with a capital letter and ends without a punctuation mark
Returns False
"""
def test_grammar_checker_for_capital_and_no_punct_returns_false():
    criteria = False
    response = grammar_checker('Hello World')
    assert criteria == response

"""
Given a string starts without a capital letter and ends with a punctuation mark
Returns False
"""

def test_grammar_checker_for_no_capital_and_punct_returns_false():
    criteria = False
    response = grammar_checker('hello World!')
    assert criteria == response

"""
Given a string starts without a capital letter and ends without a punctuation mark
Returns False
"""
def test_grammar_checker_for_no_capital_and_no_punct_returns_false():
    criteria = False
    response = grammar_checker('hello world')
    assert criteria == response
    