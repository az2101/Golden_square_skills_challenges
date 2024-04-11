# {{PROBLEM}} Function Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

_As an admin
So that I can determine whether a user is old enough
I want to allow them to enter their date of birth as a string in the format `YYYY-MM-DD`.

As an admin
So that under-age users can be denied entry
I want to send a message to any user under the age of 16 saying their access is denied, telling them their current age and the required age (16).

As an admin
So that old enough users can be granted access
I want to send a message to any user aged 16 or older to say that access has been granted.

As an admin
So that invalid entries are rejected
I want to generate an exception when the date of birth isn't the right type or format.
_

## 2. Design the Function Signature

_Include the name of the function, its parameters, return value, and side effects._

```python

def age_checker(date_of_birth):
    """Checks age is enough to grant access

    Parameters: (list all parameters and their types)
        date_of_birth - a string representing dob

    Returns: (state the return value and its type)
        a string confirming or denying entry 

    Side effects: (state any side effects)
        This function doesn't print anything or have any other side-effects
    """
    pass # Test-driving means _not_ writing any code here yet.
```

## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

```python


"""
Given an acceptable dob
returns access granted
"""
age_checker('2000-04-08') => 'Access Granted'

"""
Given an underage dob
returns access denied, their current age and age required
"""
age_checker('2012-04-08') => 'Access Denied. You are 12 years old. You must be at least 16 years old to enter!'

"""
Given an invalid dob
returns invalid
"""
age_checker('invalid') => 'Invalid date format, please try again'
```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:

```python


from lib.age_checker import *

"""
Given an acceptable dob
returns access granted
"""
def test_acceptable_age():
    criteria = 'Access Granted'
    response = age_checker('2000-04-08')
    assert criteria == response

"""
Given an underage dob
returns access denied, their current age and age required
"""
def test_too_young_age():
    criteria = 'Access Denied. You are 12 years old. You must be at least 16 years old to enter!'
    result = age_checker('2012-04-08')
    assert criteria == result


"""
Given an invalid dob
returns invalid
"""
def test_invalid_dob_format():
    criteria = 'Invalid date format, please try again'
    result = age_checker('invalid')
    assert criteria == result
    
```

Ensure all test function names are unique, otherwise pytest will ignore them!
