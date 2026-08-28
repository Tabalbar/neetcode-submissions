class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        def bottomUp(step):
            if step == 0:
                return 1
            elif step < 0:
                return 0
            if step in memo:
                return memo[step]
            res = bottomUp(step-1) + bottomUp(step-2)

            memo[step] = res
            return res

        return bottomUp(n)
        # bottomUp(5) -> # bottomUp(4) -> bu(3) -> bu2 -> bu1
        
