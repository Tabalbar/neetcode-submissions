class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = defaultdict(list)
        freq = defaultdict(int)
        return_res = []
        # nums.sort()
        for idx, num in enumerate(nums):
            res[idx] = []
            freq[num] += 1
        for key in freq:
            res[freq[key]].append(key)
        for idx in range(len(nums), -1, -1):
            if len(res[idx]) > 0:
                for num in res[idx]:
                    return_res.append(num)
                    if len(return_res) == k:
                        return return_res