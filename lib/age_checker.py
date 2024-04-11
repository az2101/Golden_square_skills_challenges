
from datetime import datetime

def age_checker(date_of_birth):
    try:
        dob = datetime.strptime(date_of_birth, '%Y-%m-%d')
    except ValueError:
        raise ValueError('Invalid date format, please try again!')
    today = datetime.today()
    age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
    
    if age < 16:
        return(f'Access Denied. You are {age} years old. You must be at least 16 years old to enter!')
    else:
        return('Access Granted')








