#It is responsible for checking whether a given expression with brackets is balanced, using a stack to match opening and closing brackets and ensuring their proper nesting.
class BracketValidator:
    def _init_(self):
        self.bracket_map = {')': '(', '}': '{', ']': '['}
<<<<<<< HEAD

    def is_balanced(self, expression):
        stack = BracketStack()

=======
    def is_balanced(self, expression):
        stack = BracketStack()
>>>>>>> d3ff1c99d1c7749d751a375cecda85f77c81a3aa
        for char in expression:
            if char in '([{':
                stack.push(char)
            elif char in ')]}':
                if not stack.is_empty() and stack.pop() == self.bracket_map[char]:
                    continue
                else:
                    return False
<<<<<<< HEAD

        return stack.is_empty()
=======
        return stack.is_empty()
>>>>>>> d3ff1c99d1c7749d751a375cecda85f77c81a3aa
