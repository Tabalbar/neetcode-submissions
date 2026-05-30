class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] = -stones[i]

        heapq.heapify(stones)
        while len(stones) > 1:
            stone1 = heapq.heappop(stones)
            stone2 = heapq.heappop(stones)

            print(stone1, stone2)
            if stone1 < stone2:
                stone1 -= stone2
                heapq.heappush(stones, stone1)
                
        if len(stones):
            return stones[0] * -1
        else:
            return 0
