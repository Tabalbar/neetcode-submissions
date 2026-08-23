class Solution:
    def isValid(self, s: str) -> bool:
        complements = {"(": ")", "[": "]", "{": "}"}
        stack = []
        for c in s:
            if c in complements:
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                complement = stack.pop()
                if c != complements[complement]:
                    return False

        return False if len(stack) else True

