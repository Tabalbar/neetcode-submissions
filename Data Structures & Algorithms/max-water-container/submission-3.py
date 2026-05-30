class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        max_area = 0

        while l < r:
            print(l, r)
            area = (r-l) * min(heights[l], heights[r])
            if area > max_area:
                max_area = area
            print(heights[l], heights[r])
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1

        return max_area