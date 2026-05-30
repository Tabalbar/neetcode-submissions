import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        nums.sort()
        self.nums = nums
        self.unique_nums = list(nums)


    def add(self, val: int) -> int:
        self.nums.append(val)
        self.nums.sort()
        self.unique_nums = list(self.nums)
        if len(self.nums) >= self.k:
            return self.nums[-self.k]
        