class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        min_heap = []
        heapq.heapify(min_heap)

        for point in points:
            distance = (math.sqrt(point[0]**2 + point[1]**2)) * -1
            heapq.heappush(min_heap, (distance, [point[0], point[1]]))
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        print(min_heap)
        return [point for _, point in min_heap]
