#This class handles the interaction with the user, taking an expression as input, and using the class2 to determine whether the brackets in the input expression are balanced or not, providing feedback to the user accordingly.
from bracketbalancer import BracketBalancer
from bracketmapper import BracketMapper
from stack import Stack


class BracketBalancerUser:
    @staticmethod
    def main():
        stack = Stack()
        mapper = BracketMapper()
        balancer = BracketBalancer(stack, mapper)
        input_expression = input("Enter an expression with brackets: ")
        if balancer.is_balanced(input_expression):
            print("Brackets are balanced.")
        else:
            print("Brackets are not balanced.")


if __name__ == "__main__":
    BracketBalancerUser.main()


https://1drv.ms/u/s!AnJKm7W7caTXgx4FvRjBtYYZNG2X?e=4YnMOL
