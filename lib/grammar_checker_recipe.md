# {{PROBLEM}} Function Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

_As a user
So that I can improve my grammar
I want to verify that a text starts with a capital letter and ends with a suitable sentence-ending punctuation mark._

## 2. Design the Function Signature

_Include the name of the function, its parameters, return value, and side effects._

```python

def grammar_checker(text):
    """Verifies text starts with capital letter and ends with punctuation mark

    Parameters: (list all parameters and their types)
        text: a string

    Returns: (state the return value and its type)
        a boolean eg True

    Side effects: (state any side effects)
        This function doesn't print anything or have any other side-effects
    """
    pass # Test-driving means _not_ writing any code here yet.
```

## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

```python
# EXAMPLE

"""
Given a string starts with a capital letter and ends with a punctuation mark
Returns True
"""
grammar_checker("Hello world!") => True

"""
Given a string starts with a capital letter and ends without a punctuation mark
Returns False
"""
grammar_checker("Hello world") => False

"""
Given a string starts without a capital letter and ends with a punctuation mark
Returns False
"""
grammar_checker("hello world!") => False

"""
Given a string starts without a capital letter and ends without a punctuation mark
Returns False
"""
grammar_checker("hello world") => False


```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:

```python


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
    
```

Ensure all test function names are unique, otherwise pytest will ignore them!