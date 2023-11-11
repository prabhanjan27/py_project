#It is responsible for checking whether a given expression with brackets is balanced, using a stack to match opening and closing brackets and ensuring their proper nesting.

class BracketValidator:
    def _init_(self, mapper):
        self.mapper = mapper

    def is_balanced(self, expression):
        stack = Stack()
        for char in expression:
            if char in '([{':
                stack.push(char)
            elif char in ')]}':
                if not stack.is_empty() and stack.pop() == self.mapper.brackets[char]:
                    continue
                else:
                    return False
        return stack.is_empty()