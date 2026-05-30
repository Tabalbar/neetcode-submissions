class Solution:
    def isValid(self, s: str) -> bool:
        dictionary_pair = {'(': ')', '[': ']', '{':'}'}
        q = deque()
        for c in s:
            if c in dictionary_pair:
                q.append(c)
            else:
                if len(q) == 0:
                    return False
                opening = q.pop()
                if c != dictionary_pair[opening]:
                    return False
        
        if len(q) == 0:
            return True
        else:
            return False