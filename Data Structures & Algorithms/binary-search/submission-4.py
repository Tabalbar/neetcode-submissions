class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = ((r - l) // 2) + l
            value = nums[mid]

            if value == target:
                return mid
            elif value > target:
                r = mid - 1
            else:
                l = mid + 1

        return -1