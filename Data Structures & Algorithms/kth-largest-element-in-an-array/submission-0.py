class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        for i in range(len(nums)):
            nums[i] = -nums[i]

        heapq.heapify(nums)
        result = -1
        for i in range(k):
            result = heapq.heappop(nums)
        result *= -1
        return result