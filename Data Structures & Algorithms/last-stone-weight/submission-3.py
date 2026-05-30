class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i,stone in enumerate(stones):
            stones[i] = -stone
        heapq.heapify(stones)

        while len(stones) > 1:
            rock1, rock2 = heapq.heappop(stones), heapq.heappop(stones)
            resulting_rock = rock1 - rock2
            print(resulting_rock, rock1, rock2)
            if resulting_rock != 0:
                heapq.heappush(stones, resulting_rock)
        heapq.heappush(stones, 0)
        return stones[0] * -1