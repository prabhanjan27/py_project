class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        """Add an item to the stack."""
        self.items.append(item)

    def pop(self):
        """Remove and return the top item from the stack."""
        return self.items.pop() if not self.is_empty() else None

    def is_empty(self):
        """Check if the stack is empty."""
        return not self.items


class BracketMapper:
    def __init__(self):
        self.brackets = {')': '(', '}': '{', ']': '['}

    def is_match(self, open_bracket, close_bracket):
        """Check if an open and close bracket form a matching pair."""
        return self.brackets.get(close_bracket) == open_bracket


class BracketValidator:
    def __init__(self, mapper):
        self.mapper = mapper

    def is_balanced(self, expression):
        """Check if the brackets in the expression are balanced."""
        stack = Stack()
        for char in expression:
            if char in '([{':
                stack.push(char)
            elif char in ')]}':
                if not stack.pop() == self.mapper.brackets[char]:
                    return False
        return stack.is_empty()


class BracketBalancer:
    def __init__(self, validator, mapper):
        self.validator = validator
        self.mapper = mapper

    def is_balanced(self, expression):
        """Check if the expression has balanced brackets."""
        return self.validator.is_balanced(expression)


class BracketBalancerUser:
    @staticmethod
    def main():
        """Entry point for the bracket balancing program."""
        mapper = BracketMapper()
        validator = BracketValidator(mapper)
        balancer = BracketBalancer(validator, mapper)

        try:
            input_expression = input("Enter an expression with brackets: ")
            if balancer.is_balanced(input_expression):
                print("Brackets are balanced.")
            else:
                print("Brackets are not balanced.")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    BracketBalancerUser.main()