#It represents a stack data structure that allows pushing and popping brackets, which is used to keep track of opening brackets as they are encountered in an expression.
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0
      class BracketMapper:
    def __init__(self):
        self.brackets = {')': '(', '}': '{', ']': '['}

    def is_match(self, open_bracket, close_bracket):
        return self.brackets.get(close_bracket) == open_bracket
