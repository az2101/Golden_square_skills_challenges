
class DiaryEntry:
    def __init__(self, title, contents):
        if title == "" or contents == "":
            raise Exception("Diary entries must have a title or contents")
        self.title = title
        self.contents = contents
        self._read_so_far = 0

    def format(self):
        return f"{self.title}: {self.contents}"

    def count_words(self):
        return len(self.title.split()) + len(self.contents.split())
    

    def reading_time(self, wpm):
        contents_words = len(self.contents.split())
        return contents_words / wpm

    def reading_chunk(self, wpm, minutes):
        readable_amount = wpm * minutes
        contents_word_list = self.contents.split()
        if self._read_so_far >= len(contents_word_list):
            self._read_so_far = 0

        readable_words = contents_word_list[self._read_so_far:self._read_so_far + readable_amount]
        self._read_so_far += readable_amount
        return ' '.join(readable_words)
    
