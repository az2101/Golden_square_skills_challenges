
class GrammarStats:
    def __init__(self):
        self.total_checked = 0
        self.total_passed = 0

    def check(self, text):
        if text == '':
            pass
        elif text[0].isupper() and text[-1] in '?.!':
            self.total_checked += 1
            self.total_passed += 1
            return True
        else:
            self.total_checked += 1
            return False

    def percentage_good(self):
        return (self.total_passed / self.total_checked) * 100
