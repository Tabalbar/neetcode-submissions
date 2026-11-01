class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        buckets = {x:[] for x in range(len(nums)+1)}
        freq = Counter(nums)
        for num in freq:
            buckets[freq[num]].append(num)
        for num in range(len(nums), -1, -1):
            if len(buckets[num]) > 0:
                for val in buckets[num]:
                    res.append(val)
                    if len(res) >= k:
                        return res
