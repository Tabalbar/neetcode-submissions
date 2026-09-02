class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        max_heap = [(freq[key], key) for key in freq]
        heapq.heapify(max_heap)
        while len(max_heap) > k:
            heapq.heappop(max_heap)

        return [val[1] for val in max_heap]
