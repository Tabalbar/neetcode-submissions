class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False

        stack = []

        for letter in s:
            if letter == '[':
                stack.append('[')
            elif letter == '{':
                stack.append('{')
            elif letter == '(':
                stack.append('(')
            elif (letter == ']'):
                if len(stack) == 0 or stack.pop() != '[':
                    return False
            elif (letter == '}'):
                if len(stack) == 0 or stack.pop() != '{':
                    return False
            elif (letter == ')'):
                if len(stack) == 0 or stack.pop() != '(':
                    return False
        if len(stack) > 0:
            return False
        else:
            return True
            
