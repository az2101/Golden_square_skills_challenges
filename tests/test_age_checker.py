
import pytest
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
    with pytest.raises(ValueError):
        age_checker('invalid')





