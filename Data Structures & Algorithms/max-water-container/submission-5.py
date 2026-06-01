class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights)-1
        max_area = 0
        while l < r:
            lnum = heights[l]
            rnum = heights[r]
            height = min(lnum, rnum)
            width = r - l
            prod = height * width
            if prod > max_area:
                max_area = prod

            if lnum < rnum:
                l += 1
            else:
                r -= 1

        return max_area