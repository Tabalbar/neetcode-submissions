class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            if l == r:
                return nums[l]

            mid = l + ((r - l)//2)

            if nums[l] <= nums[mid] and nums[l] < nums[r]:
                return nums[l]
            elif nums[mid] < nums[r] and nums[mid] < nums[l]:
                r = mid
            else:
                l = mid + 1

        

