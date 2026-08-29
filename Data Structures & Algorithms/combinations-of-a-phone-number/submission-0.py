class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        result = []
        subset = []
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }
        def processDigits(n):
            nonlocal subset
            if n == len(digits):
                print(result)
                if len(subset.copy()):
                    result.append("".join(subset.copy()))
                return
            for c in digitToChar[digits[n]]:
                subset.append(c)
                processDigits(n+1)
                subset.pop()


        processDigits(0)


        return result