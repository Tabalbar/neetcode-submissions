class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        tracker = []
        def backTrack(n, subset):
            if n == 0:
                if len(tracker) == 0:
                    result.append("".join(subset))
                    return
            else:
                subset.append("(")
                tracker.append("(")
                backTrack(n-1, subset)
                tracker.pop()
                subset.pop()
            if tracker:
                subset.append(")")
                tracker.pop()
                backTrack(n, subset)
                subset.pop()
                tracker.append("(")

        backTrack(n, [])
        print(result)
        return result