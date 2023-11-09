class BracketMapper:
    def __init__(self):
        self.brackets = {')': '(', '}': '{', ']': '['}

    def is_match(self, open_bracket, close_bracket):
        return self.brackets.get(close_bracket) == open_bracket
