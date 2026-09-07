class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = {}
        def dfs(r, c):
            if r >= m or c >= n:
                return 0
            elif r == m-1 and c == n-1:
                return 1
            if f"({r},{c})" in memo:
                return memo[f"({r},{c})"]
            total = 0
            total += dfs(r + 1, c)
            total += dfs(r, c + 1)

            memo[f"({r},{c})"] = total
            
            return total


        return dfs(0,0)