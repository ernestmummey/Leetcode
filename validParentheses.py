# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.

# This will run in O(n) time and O(n) space
def validParentheses(arr):
    stack = []
    opening_brackets = '{[('
    closing_brackets = '}])'
    matching_brackets = {'}':'{', ']':'[', ')':'('}
#   first iterate through the arr
    for char in arr:
#       Then check to see if the char in the array matches the opening_brackets
        if char in opening_brackets:
#           if it does the append the char into the stack
            stack.append(char)
#       if it matches the closing brackets
        elif char in closing_brackets:
#           check to see if the stack length is empty
            if len(stack):
#               We will then return false as the brackets would be out of order
                return False
#           If the lasting char in the stack matches any og the matching brackets
            if stack[-1] == matching_brackets:
                stack.pop()
            else:
                return False
#   There is really nothing to return except to see if the stack length is equal to zero 
    return len(stack) == 0



