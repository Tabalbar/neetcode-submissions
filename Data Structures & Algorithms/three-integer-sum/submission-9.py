class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = set()
        nums.sort()

        for idx, num in enumerate(nums):
            l = idx +1
            r = len(nums)-1

            while l < r:
                left = nums[l]
                right = nums[r]
                total = num + left + right

                if total < 0:
                    l +=1
                elif total > 0:
                    r -=1
                else:
                    result.add((num, left, right))
                    l += 1
                    r -= 1

        return [list(t) for t in result]