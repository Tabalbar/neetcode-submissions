class Solution:
    def climbStairs(self, n: int) -> int:
        cache = {}
        def topDown(n):
            if n in cache:
                return cache[n]
            if n < 0:
                cache[n] = 0
                return 0
            elif n == 0:
                cache[n] = 1
                return 1



            result = topDown(n-2) + topDown(n-1)
            cache[n] = result
            return result
            # [1]->[0]
            # [2]->[1][0]->[0]

        return topDown(n)