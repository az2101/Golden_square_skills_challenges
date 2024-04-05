# {{PROBLEM}} Function Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

_Design a function that takes a string and returns the number of words in the string_

## 2. Design the Function Signature

_Include the name of the function, its parameters, return value, and side effects._

```python
# EXAMPLE

def count_words(string):
    """Counts number of words in string

    Parameters: (list all parameters and their types)
        string: a string containing words (e.g. "hello WORLD")

    Returns: (state the return value and its type)
        an integer represeting the number of words in the string

    Side effects: (state any side effects)
        This function doesn't print anything or have any other side-effects
    """
    pass # Test-driving means _not_ writing any code here yet.
```

## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

```python


"""
Given an empty string it returns 0
"""
count_words('') => 0

"""
Given a string of one words it returns 1
"""
count_words('Hello') => 1

"""
Given a string of two words it returns 2
"""
count_words('Hello world') => 2

"""
Given a string of five words it returns 5
"""
count_words('Hello my name is Andrew') => 5
```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:

```python

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

```

Ensure all test function names are unique, otherwise pytest will ignore them!