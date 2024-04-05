
def make_snippet(string):
    split_string = string.split()
    if len(split_string) > 5:
        first_5_list = split_string[0:5]
        first_5_string = ' '.join(first_5_list) + '...'
        return first_5_string
    else:
        return (string)    



