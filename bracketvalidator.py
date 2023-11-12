class BracketValidator:
    def _init_(self, mapper):
        self.mapper = mapper
    def is_balanced(self, expression): 
        stack = Stack()
        for char in expression:
            if char in '([{':
                stack.push(char)
            elif char in ')]}':
                if not stack.pop() == self.mapper.brackets[char]:
                    return False
        return stack.is_empty()
