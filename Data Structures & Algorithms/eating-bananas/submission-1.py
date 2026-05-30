class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        min_eat_rate = r
        while l <= r:
            mid = l + ((r-l)//2)
            res = 0
            print(mid)
            copy_piles = list(piles)
            for pile in piles:
                res += math.ceil(pile/mid)
            print(res)
            if res > h:
                l = mid + 1
            else:
                r = mid - 1
                min_eat_rate = mid
        return min_eat_rate
            



