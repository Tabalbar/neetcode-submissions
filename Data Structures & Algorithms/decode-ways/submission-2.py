class Solution:
    def numDecodings(self, s: str) -> int:
        memo = {}

        def dfs(n):
            if n >= len(s):
                return 1

            if n in memo:
                return memo[n]

            total = 0
            curr = s[n]
            if curr != "0":
                total += dfs(n+1)
                
            if n + 1 < len(s):
                curr += s[n + 1]
                if "10" <= str(curr) <= "26":  
                    total += dfs(n + 2)

            memo[n] = total
            return total
        return dfs(0)

        # 1. 
        # send first index
        # decode first char and add letter to array
        # 2. 
        # send second index
        # decode second char and add letter to array
        # but also need a run for getting second index and add letter to array

        # 1. 
        # send 2nd index
        # decode first char as two characters and add letter to array
        # 2. 
        # decode second char as 1 character and add letter to array
        # decode second char as 2 characters and add letter to array


